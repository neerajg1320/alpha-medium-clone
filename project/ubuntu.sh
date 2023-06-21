sudo mkdir -p /etc/apt/keyrings
curl -fsS https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" |sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo docker --version
sudo docker compose version
sudo ufw status numbered
sudo ufw allow 22/tcp
sudo ufw enable

sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 81

# Setup nginx ProxyManager

# Setup portainer
sudo docker run -d -p 8000:8000 --network=reverseproxy_nw --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest