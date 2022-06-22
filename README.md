the repo are add by using SSH key:
sudo nano ~/.ssh/config
** Host github.com
**  Hostname ssh.github.com
**  Port 443
ssh -T git@github.com

git push -u origin main