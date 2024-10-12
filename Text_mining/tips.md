# dockerのインストール  
**1.必要なパッケージのインストール**  
~~~
sudo apt-get update
sudo apt-get install \ 
    ca-certificates \
    curl \
    gnupg \
    lsb-release
~~~

**2.Docker の GPG 鍵を追加**  
~~~
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
~~~

**3.Docker リポジトリを追加**  
~~~
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
~~~

**3-2.ulyssaが使用できない場合、focalを使用する**  
~~~
sudo sed -i 's/ulyssa/focal/g' /etc/apt/sources.list.d/docker.list
sudo sed -i 's/ulyssa/focal/g' /etc/apt/sources.list.d/additional-repositories.list
~~~

**4.Docker をインストール**  
~~~
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
~~~

**5.インストールの確認**  
~~~
sudo docker --version
~~~

**6.ユーザーを docker グループに追加（オプション）**  
~~~
sudo usermod -aG docker $USER
newgrp docker
id
~~~
>> gid=999(docker) となっていればOK  

**7.コンテナの立ち上げ**  
~~~
docker compose up (-d)
~~~

