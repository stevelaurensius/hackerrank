result = set()

eng_subscriber = int(input())
result = set(input().split())
frn_subscriber = int(input())
result = result.union(input().split())

print(len(result))