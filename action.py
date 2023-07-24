import requests
from github import Auth, Github
import sys
from pprint import pprint

# raw_branch = sys.argv[1]


# 用您自己的 GitHub Token 初始化 Github 对象
github_token = "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"



r = requests.get(
    "https://api.github.com/repos/Henry-Li-PNTL/test-action",
    headers= {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
)
r.raise_for_status()
# pprint(r.json())



r = requests.get(
    "https://api.github.com/repos/Henry-Li-PNTL/test-action/pulls/5",
    headers= {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
)

# pprint(r.json())


print(f"Merge {r.json()['head']['ref']} to {r.json()['base']['ref']}")

exit()








# ====================================================================================
auth = Auth.Token("access_token")
g = Github(auth=auth)

# 您的 GitHub 仓库的所有 Pull Requests
repo = g.get_repo("Henry-Li-PNTL/test-action")
pull_number = 5
# pull_number = int( raw_branch.split("/")[2] )
# pull_number = 42  # 用实际的 Pull Request 编号替换这里

# 获取指定 Pull Request 的信息
pull_request = repo.get_pull(pull_number)

# 获取合并的分支（base）和来源分支（head）
base_branch = pull_request.base.ref
source_branch = pull_request.head.ref

print(f"Pull Request #{pull_number} 合并的分支是: {base_branch}")
print(f"Pull Request #{pull_number} 来源分支是: {source_branch}")
# ====================================================================================
