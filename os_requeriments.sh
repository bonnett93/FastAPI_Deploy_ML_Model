# Adicitional installations for ubuntu os
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential libssl-dev
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
git lfs track "*.psd"
git add .gitattributes
