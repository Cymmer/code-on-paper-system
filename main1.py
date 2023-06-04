import os
import io
import openai
import requests
import numpy as np
import pandas as pd
from PIL import Image
from google.cloud import vision
from Preprocess import clean_img, scale_image, enhance_image
from analysis import string_similarity, minify_c_code
from test_cases import get_request_body_test_cases, get_test_cases, get_labels_and_prompts
from insensitive_checking import insensitive_checking_preprocessing


problem_number = 1
openai.api_key = os.getenv("OPEN_AI_SECRET_KEY")
rootdir = f"/Users/cymmerjohnmaranga/Downloads/Problem{problem_number}_new copy"

file_paths = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_path = subdir + os.sep + file
        file_paths.append(file_path)


scale_factor = 2
# Preprocess images
for i, file_path in enumerate(file_paths):
    try:
        image = Image.open(file_path)
        np_image = np.array(image)
        cleaned_image = clean_img(np_image)
        img = Image.fromarray(np.uint8(cleaned_image))
        scaled_img = scale_image(img, scale_factor)
        enhanced_img = enhance_image(scaled_img)
        enhanced_img.save(file_path)
    except Exception as e:
        print("ERROR: ", e)

file_paths.sort()

IDS = []
imageLinks = []
googleVisionAPIResults = []
openAIAPIResults = []
checkerStatuses = []

for i, file_path in enumerate(file_paths):
    if file_path.split(".")[-1] not in ["png", "jpg"]:
        continue

    ### GOOGLE CLOUD VISION ###
    client = vision.ImageAnnotatorClient()
    with io.open(file_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    detections = response.full_text_annotation
    converted_text = detections.text

    ### OPEN AI ###
    model = "gpt-3.5-turbo"
    body = f"Make this C code snippet syntax-error free only. Do not add additional code that may change the overall logic of the code. \n\n{converted_text}"
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": body}],
        )
    except (openai.APIError, openai.InvalidRequestError, openai.OpenAIError) as e:
        print("OPEN AI ERROR: ", e)
        pass

    corrected_code = completion.choices[0].message.content
    test_cases = get_request_body_test_cases(problem_number=problem_number, code=corrected_code)
    response = requests.post(
        "https://codechum-interactive-svjuxd2qva-de.a.run.app/v1/interactive/checker",
        json=test_cases,
    )

    data = response.json()
    is_correct = all(
        regex_status["is_correct"] for regex_status in data["regex_statuses"]
    )

    if is_correct:
        for i, submission in enumerate(data["submissions"]):
            status = submission[list(submission.keys())[0]]["status"]
            if status != 3:
                is_correct = False
                break

            stdout = submission[list(submission.keys())[0]]["stdout"]

            labels_and_prompts = get_labels_and_prompts(problem_number=problem_number)
            
            for label_and_prompt in labels_and_prompts:
                stdout = stdout.replace(label_and_prompt, "")

            print(stdout)

            preprocessed_stdout = insensitive_checking_preprocessing(stdout)
            preprocessed_test_case_stdout = insensitive_checking_preprocessing(
                get_test_cases(problem_number=problem_number)[i]
            )

            if preprocessed_stdout != preprocessed_test_case_stdout:
                print("PREPROCESSED_STDOUT: ", preprocessed_stdout)
                print("PREPROCESSED_TEST_CASE_STDOUT", preprocessed_test_case_stdout)
                is_correct = False
                break

    IDS.append(i)
    imageLinks.append(file_path)
    googleVisionAPIResults.append(converted_text)
    openAIAPIResults.append(corrected_code)
    checkerStatuses.append(is_correct)

# Excel Settings
excel_file_path = (
    f"/Users/cymmerjohnmaranga/Downloads/ExcelDatasets_New/C_Problem{problem_number}_New.xlsx"
)
sheet_name = f"Problem{problem_number}"

with open(f"./problems/problem{problem_number}.c", "r") as f:
    actual_problem_code = f.read()

problem_data = pd.DataFrame(
    {
        "ID": IDS,
        "Image Link": imageLinks,
        "Google Vision API Results": googleVisionAPIResults,
        "Open AI Results": openAIAPIResults,
        "Actual Codes": [actual_problem_code for _ in range(len(openAIAPIResults))],
        "Google Vision API Results (MINIFIED)": [
            minify_c_code(code) for code in googleVisionAPIResults
        ],
        "Open AI Results (MINIFIED)": [
            minify_c_code(code) for code in openAIAPIResults
        ],
        "Actual Codes (MINIFIED)": [
            minify_c_code(actual_problem_code) for _ in range(len(openAIAPIResults))
        ],
        "Google Vision API Result vs Corrected Code": [
            string_similarity(
                minify_c_code(googleVisionAPIResults[i]),
                minify_c_code(openAIAPIResults[i]),
            )
            for i in range(len(openAIAPIResults))
        ],
        "Corrected Code vs Actual Code": [
            string_similarity(
                minify_c_code(openAIAPIResults[i]), minify_c_code(actual_problem_code)
            )
            for i in range(len(openAIAPIResults))
        ],
        "Checker Status": checkerStatuses,
    }
)

sheets = {f"Problem{problem_number}": problem_data}
writer = pd.ExcelWriter(excel_file_path, engine="xlsxwriter")

for sheet_name in sheets.keys():
    sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()
