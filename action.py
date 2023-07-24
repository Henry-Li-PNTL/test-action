from github import Github
from github import Github

# Authentication is defined via github.Auth
from github import Auth
import sys

raw_branch = sys.argv[1]


# 用您自己的 GitHub Token 初始化 Github 对象
github_token = "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"
g = Github(Auth.Token(github_token))

# 您的 GitHub 仓库的所有 Pull Requests
repo = g.get_repo("Henry-Li-PNTL/test-action")
pull_number = int( raw_branch.split("/")[2] )
# pull_number = 42  # 用实际的 Pull Request 编号替换这里

# 获取指定 Pull Request 的信息
pull_request = repo.get_pull(pull_number)

# 获取合并的分支（base）和来源分支（head）
base_branch = pull_request.base.ref
source_branch = pull_request.head.ref

print(f"Pull Request #{pull_number} 合并的分支是: {base_branch}")
print(f"Pull Request #{pull_number} 来源分支是: {source_branch}")
