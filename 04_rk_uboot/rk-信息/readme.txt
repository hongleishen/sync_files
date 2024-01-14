钱统计
    python在 ubuntu中执行
    
     git push -u origin init


     

topeet@ubuntu:~/wks/00_vscode_wks/sync_file$ git remote add origin git@github.com:hongleishen/sync_files.git

topeet@ubuntu:~/wks/00_vscode_wks/sync_file$ git branch -a
* init

topeet@ubuntu:~/wks/00_vscode_wks/sync_file$ git push -u origin init
对象计数中: 4, 完成.
Delta compression using up to 4 threads.
压缩对象中: 100% (4/4), 完成.
写入对象中: 100% (4/4), 12.47 KiB | 4.16 MiB/s, 完成.
Total 4 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'init' on GitHub by visiting:
remote:      https://github.com/hongleishen/sync_files/pull/new/init
remote:
To github.com:hongleishen/sync_files.git
 * [new branch]      init -> init
分支 'init' 设置为跟踪来自 'origin' 的远程分支 'init'。


topeet@ubuntu:~/wks/00_vscode_wks/sync_file$ git branch -a
* init
  remotes/origin/init



本地创建分支，修改，远程创建分支并推送到远程
git checkout -b 1103

....

git push -u origin 1103