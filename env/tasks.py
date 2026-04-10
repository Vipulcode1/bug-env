TASKS = [
    {
        "id": "easy",
        "code": 'print("hello"',
        "tests": ["True"]
    },
    {
       
    "id": "medium",
    "code": "",
    "tests": ["add(2,3)==5"]

    },
    {
    "id": "hard",
    "code": '''
def process(nums):
    result = []
    for n in nums:
        if n % 2 == 1:
            result.append(n*2)
    return result
''',
    "tests": [
        "process([1,2,3])==[2,6]",
        "process([2,4])==[]",
        "process([5])==[10]"
    ]
}
]