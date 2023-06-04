def get_labels_and_prompts(problem_number):
    if problem_number == 1:
        return ["Input:", "Enter your name:", "Enter your age:", "Output: ", "Your name is", "and you are", "years old"]

def get_request_body_test_cases(problem_number, code):
    if problem_number == 1:
        return {
            "is_file_handling": False,
            "test_cases": [
                {"0": ["Cymmer John Maranga\n23"]},
                {"1": ["Jefferson Abellanosa\n23"]},
                {"2": ["Monica Pillones\n100"]},
            ],
            "regex_test_cases": [
                {
                    "id": 2970,
                    "description": "Should use instructed regular expression printf\\s*\\(",
                    "regex": "printf\\s*\\(",
                    "problem_id": 6283,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 22:48:08 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2971,
                    "description": "Should use instructed regular expression scanf\\s*\\(",
                    "regex": "scanf\\s*\\(",
                    "problem_id": 6283,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 22:48:08 GMT+0800",
                    "deleted": None,
                },
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 2:
        return {
            "is_file_handling": False,
            "test_cases": [
                {"0": ["10\n20.43\n22.15\nh"]},
                {"1": ["10000\n32.04\n54.2223\nn"]},
                {"2": ["873\n76.3\n123.546\nh"]},
            ],
            "regex_test_cases": [
                {
                    "id": 2972,
                    "description": "Should use instructed regular expression \\bint\\s+",
                    "regex": "\\bint\\s+",
                    "problem_id": 6286,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 23:53:50 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2973,
                    "description": "Should use instructed regular expression \\bfloat\\s+",
                    "regex": "\\bfloat\\s+",
                    "problem_id": 6286,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 23:53:50 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2974,
                    "description": "Should use instructed regular expression \\bdouble\\s+",
                    "regex": "\\bdouble\\s+",
                    "problem_id": 6286,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 23:53:50 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2975,
                    "description": "Should use instructed regular expression \\bchar\\s+",
                    "regex": "\\bchar\\s+",
                    "problem_id": 6286,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/21/2023 23:53:50 GMT+0800",
                    "deleted": None,
                },
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 3:
        return {
            "is_file_handling": True,
            "test_cases": [{"0": ["5\n3"]}, {"1": ["7\n3"]}, {"2": ["10\n9"]}],
            "regex_test_cases": [],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 4:
        return {
            "is_file_handling": False,
            "test_cases": [{"0": ["4\n5"]}, {"1": ["5\n5"]}, {"2": ["100\n5"]}],
            "regex_test_cases": [
                {
                    "id": 2978,
                    "description": "Should use if-else if statement",
                    "regex": "\\s*if\\s*\\(.+\\)[\\s\\S]*else if\\s*\\(.+\\)[\\s\\S]*|\\s*if[\\s\\S]*\\s*elif[\\s\\S]*[\\s\\S]*",
                    "problem_id": 6288,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 00:41:50 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2979,
                    "description": "Should use instructed regular expression else\\s*{",
                    "regex": "else\\s*{",
                    "problem_id": 6288,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 00:41:50 GMT+0800",
                    "deleted": None,
                },
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 5:
        return {
            "is_file_handling": False,
            "test_cases": [{"0": ["1"]}, {"1": ["0"]}, {"2": ["5"]}],
            "regex_test_cases": [
                {
                    "id": 2980,
                    "description": "Should use instructed regular expression switch\\s*\\(.+\\)\\s*{",
                    "regex": "switch\\s*\\(.+\\)\\s*{",
                    "problem_id": 6289,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 00:45:22 GMT+0800",
                    "deleted": None,
                }
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 6:
        return {
            "is_file_handling": False,
            "test_cases": [
                {"0": ["1\n0\n1\n-1"]},
                {"1": ["-5"]},
                {"2": ["50\n50\n50\n0\n-1"]},
            ],
            "regex_test_cases": [
                {
                    "id": 2981,
                    "description": "Should use do-while loop",
                    "regex": "(\\s*do\\s*{[\\s\\S]*\\}\\s*while\\s*\\([\\s*\\S]*\\);)",
                    "problem_id": 6290,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 00:54:07 GMT+0800",
                    "deleted": None,
                }
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 7:
        return {
            "is_file_handling": False,
            "test_cases": [{"0": ["5"]}, {"1": ["3"]}, {"2": ["1"]}],
            "regex_test_cases": [
                {
                    "id": 2982,
                    "description": "Should use for loop",
                    "regex": "(\\s*for\\s*\\(.+\\))|for[\\s\\S]*(in|range)\\s*(\\w*)|\\(.*\\)",
                    "problem_id": 6291,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 00:58:23 GMT+0800",
                    "deleted": None,
                }
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": '#include <stdio.h>\nint main() {\n    int n;\n    printf("Enter n: ");\n    scanf("%d", &n);\n    int sum = 0;\n    for(int i = 1; i <= n; i++) {\n        sum += i;\n    }\n    printf("Output: The sum of the first %d natural numbers is %d", n, sum);\n    return 0;\n}',
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 8:
        return {
            "is_file_handling": False,
            "test_cases": [
                {"0": ["1 2 3 4 5 6 7 8 9 10"]},
                {"1": ["1 -1 1 -1 2 -2 2 -2 3 -3"]},
                {"2": ["0 0 0 100000 0 0 10000 0 0 11111"]},
            ],
            "regex_test_cases": [
                {
                    "id": 2983,
                    "description": "Should use arrays",
                    "regex": "\\[.*\\]",
                    "problem_id": 6292,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:01:50 GMT+0800",
                    "deleted": None,
                }
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 9:
        return {
            "is_file_handling": False,
            "test_cases": [{"0": ["3"]}, {"1": ["-110011"]}, {"2": ["10"]}],
            "regex_test_cases": [
                {
                    "id": 2985,
                    "description": "Should use instructed regular expression \\bint\\s*\\*\\s*\\w+",
                    "regex": "\\bint\\s*\\*\\s*\\w+",
                    "problem_id": 6293,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:06:46 GMT+0800",
                    "deleted": None,
                }
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }

    if problem_number == 10:
        return {
            "is_file_handling": False,
            "test_cases": [
                {"0": ["J\n8\n7.666\n6.555"]},
                {"1": ["H\n-5\n10.1\n-25.3"]},
                {"2": ["A\n0\n0\n0"]},
            ],
            "regex_test_cases": [
                {
                    "id": 2997,
                    "description": "Should use function char getCharacter",
                    "regex": "[mM]ain[\\s\\S]*char getCharacter\\(.*\\)\\s*;|[\\s\\S]char getCharacter\\s*\\(.*\\)|char getCharacter\\([\\s\\S]*\\)",
                    "problem_id": 6294,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:24:28 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2998,
                    "description": "Should use function void printMessage",
                    "regex": "[mM]ain[\\s\\S]*void printMessage\\(.*\\)\\s*;|[\\s\\S]void printMessage\\s*\\(.*\\)|void printMessage\\([\\s\\S]*\\)",
                    "problem_id": 6294,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:24:28 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 2999,
                    "description": "Should use function int decrement",
                    "regex": "[mM]ain[\\s\\S]*int decrement\\(.*\\)\\s*;|[\\s\\S]int decrement\\s*\\(.*\\)|int decrement\\([\\s\\S]*\\)",
                    "problem_id": 6294,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:24:28 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 3000,
                    "description": "Should use function float half",
                    "regex": "[mM]ain[\\s\\S]*float half\\(.*\\)\\s*;|[\\s\\S]float half\\s*\\(.*\\)|float half\\([\\s\\S]*\\)",
                    "problem_id": 6294,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:24:28 GMT+0800",
                    "deleted": None,
                },
                {
                    "id": 3001,
                    "description": "Should use function double fourth",
                    "regex": "[mM]ain[\\s\\S]*double fourth\\(.*\\)\\s*;|[\\s\\S]double fourth\\s*\\(.*\\)|double fourth\\([\\s\\S]*\\)",
                    "problem_id": 6294,
                    "is_codechum_requirement": True,
                    "datetime_updated": "04/22/2023 01:24:28 GMT+0800",
                    "deleted": None,
                },
            ],
            "programming_language_id": 1,
            "source_codes": [
                {
                    "code": code,
                    "file_name": "main",
                    "file_extension": "c",
                }
            ],
            "mode": "interactive",
        }


def get_test_cases(problem_number):
    if problem_number == 1:
        return [
            "Input:\nEnter your name: Cymmer John Maranga\nEnter your age: 23\nOutput:\nYour name is Cymmer John Maranga and you are 23 years old.",
            "Input:\nEnter your name: Jefferson Abellanosa\nEnter your age: 23\nOutput:\nYour name is Jefferson Abellanosa and you are 23 years old.",
            "Input:\nEnter your name: Monica Pillones\nEnter your age: 100\nOutput:\nYour name is Monica Pillones and you are 100 years old.",
        ]

    if problem_number == 2:
        return [
            "Enter integer value: 10\nEnter floating-point value: 20.43\nEnter double-precision value: 22.15\nEnter a character: h\nGathered Inputs: \nint: 10\nfloat: 20.43\ndouble: 22.15\nchar: h",
            "Enter integer value: 10000\nEnter floating-point value: 32.04\nEnter double-precision value: 54.2223\nEnter a character: n\nGathered Inputs: \nint: 10000\nfloat: 32.04\ndouble: 54.22\nchar: n",
            "Enter integer value: 873\nEnter floating-point value: 76.3\nEnter double-precision value: 123.546\nEnter a character: h\nGathered Inputs: \nint: 873\nfloat: 76.30\ndouble: 123.55\nchar: h",
        ]

    if problem_number == 3:
        return [
            "Enter 1st value: 5\nEnter 2nd value: 3\nAddition: 8\nSubtraction: 2\nMultiplication: 15\nDivision: 1.67\nModulo: 2",
            "Enter 1st value: 7\nEnter 2nd value: 3\nAddition: 10\nSubtraction: 4\nMultiplication: 21\nDivision: 2.33\nModulo: 1",
            "Enter 1st value: 10\nEnter 2nd value: 9\nAddition: 19\nSubtraction: 1\nMultiplication: 90\nDivision: 1.11\nModulo: 1",
        ]

    if problem_number == 4:
        return [
            "Input: \nEnter the first integer: 4\nEnter the second integer: 5\nOutput: \nThe second integer is larger.",
            "Input: \nEnter the first integer: 5\nEnter the second integer: 5\nOutput: \nThe two integers are equal.",
            "Input: \nEnter the first integer: 100\nEnter the second integer: 5\nOutput: \nThe first integer is larger.",
        ]

    if problem_number == 5:
        return [
            "Enter input: 1\nOutput: ON",
            "Enter input: 0\nOutput: OFF",
            "Enter input: 5\nOutput: ERR",
        ]

    if problem_number == 6:
        return [
            "Enter value: 1\nPiggy Bank: 1\nEnter value: 0\nPiggy Bank: 1\nEnter value: 1\nPiggy Bank: 2\nEnter value: -1\nPiggy Bank Broken",
            "Enter value: -5\nPiggy Bank Broken",
            "Enter value: 50\nPiggy Bank: 50\nEnter value: 50\nPiggy Bank: 100\nEnter value: 50\nPiggy Bank: 150\nEnter value: 0\nPiggy Bank: 150\nEnter value: -1\nPiggy Bank Broken",
        ]

    if problem_number == 7:
        return [
            "Enter n: 5\nOutput: The sum of the first 5 natural numbers is 15",
            "Enter n: 3\nOutput: The sum of the first 3 natural numbers is 6",
            "Enter n: 1\nOutput: The sum of the first 1 natural numbers is 1",
        ]

    if problem_number == 8:
        return [
            "Enter 10 integers: 1 2 3 4 5 6 7 8 9 10\nOutput: [1,2,3,4,5,6,7,8,9,10]",
            "Enter 10 integers: 1 -1 1 -1 2 -2 2 -2 3 -3\nOutput: [1,-1,1,-1,2,-2,2,-2,3,-3]",
            "Enter 10 integers: 0 0 0 100000 0 0 10000 0 0 11111\nOutput: [0,0,0,100000,0,0,10000,0,0,11111]",
        ]

    if problem_number == 9:
        return [
            "Original value: 10\nEnter new value: 3\nNew value: 3",
            "Original value: 10\nEnter new value: -110011\nNew value: -110011",
            "Original value: 10\nEnter new value: 10\nNew value: 10",
        ]

    if problem_number == 10:
        return [
            "Enter the first char of your name: J\nEnter an integer: 8\nEnter a float: 7.666\nEnter a double: 6.555\nWelcome, J!\nDecremented int is: 7\nHalved float is: 3.83\nFourth of double is: 1.64",
            "Enter the first char of your name: H\nEnter an integer: -5\nEnter a float: 10.1\nEnter a double: -25.3\nWelcome, H!\nDecremented int is: -6\nHalved float is: 5.05\nFourth of double is: -6.33",
            "Enter the first char of your name: A\nEnter an integer: 0\nEnter a float: 0\nEnter a double: 0\nWelcome, A!\nDecremented int is: -1\nHalved float is: 0.00\nFourth of double is: 0.00",
        ]
