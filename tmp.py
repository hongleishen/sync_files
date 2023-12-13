本地创建分支，修改，创建远程分支并推送到远程

$ git push -u origin 1211
枚举对象中: 9, 完成.
对象计数中: 100% (9/9), 完成.
使用 8 个线程进行压缩
压缩对象中: 100% (5/5), 完成.
写入对象中: 100% (5/5), 489 字节 | 489.00 KiB/s, 完成.
总共 5 （差异 4），复用 0 （差异 0）
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
remote:
remote: Create a pull request for '1211' on GitHub by visiting:
remote:      https://github.com/hongleishen/sync_files/pull/new/1211
remote:
To github.com:hongleishen/sync_files.git
 * [new branch]      1211 -> 1211
分支 '1211' 设置为跟踪来自 'origin' 的远程分支 '1211'。





$ git branch -a
  1103
* 1211
  main
  remotes/origin/1103
  remotes/origin/1211

$ git branch -vv
  1103  bae6362 [origin/1103] money update to 1204
* 1211  d4fe931 [origin/1211] try 1211 branch





shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$ git branch -a
  1103
* 1211
  1211_
  main
  remotes/origin/1103
  remotes/origin/1211
  remotes/origin/HEAD -> origin/main
  remotes/origin/init
  remotes/origin/main
  remotes/origin/origin/1103

shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$ git push origin --delete origin/1103
To github.com:hongleishen/sync_files.git
 - [deleted]         origin/1103

shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$ git branch -a
  1103
* 1211
  1211_
  main
  remotes/origin/1103
  remotes/origin/1211
  remotes/origin/HEAD -> origin/main
  remotes/origin/init
  remotes/origin/main



shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$ git push origin --delete 1103
To github.com:hongleishen/sync_files.git
 - [deleted]         1103
shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$
shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$
shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$
shl@qk-Vostro-3671:~/wks/01_vs_wks/sync_files$ git branch -a
  1103
* 1211
  1211_
  main
  remotes/origin/1211
  remotes/origin/HEAD -> origin/main
  remotes/origin/init
  remotes/origin/main


  git push origin --delete origin/1103          # 删除 remotes/origin/origin/1103

  #                        远程分支省略 remotes/origin
  git push origin --delete 1103                 # remotes/origin/1103
  #                    远程分支省略 remotes/origin
  git push origin 1211:1212                     # remotes/origin/1212