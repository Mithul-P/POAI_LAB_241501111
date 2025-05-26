knowledge_base = [
    (["cough", "fever"], "flu"),
    (["sore_throat", "runny_nose"], "cold"),
    (["sore_throat"], "fever")
]

facts = {"cough", "sore_throat"}

def forward_chaining():
    inferred = True
    while inferred:
        inferred = False
        for conditions, conclusion in knowledge_base:
            if conclusion not in facts and all(cond in facts for cond in conditions):
                facts.add(conclusion)
                inferred = True

forward_chaining()
print("Inferred facts:", facts)
