# Three-Tier-Architecture-Implementation

This project shows a simple **3-tier app** on Azure:
- **Frontend VM** → Apache + HTML (proxy to backend)
- **Backend VM** → Flask PYTHON API
- **Database VM** → MySQL with demo data

---

## ⚙️ Setup Steps

## Step 1. Create VMs
- Frontend VM (Ubuntu, port 80 open)
- Backend VM (Ubuntu, port 5000 open)
- Database VM (Ubuntu, port 3306 open)

All VMs must be in the same **Azure VNET**.

---

## Step 2. Setup Database VM
```bash
sudo apt update && sudo apt install mysql-server -y
sudo mysql < database/schema.sql

**Edit MySQL bind address**:
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
Change : bind-address = 0.0.0.0

**Restart MySQl:**
sudo systemctl restart mysql
.


## Step 3. Setup Backend VM

sudo apt update && sudo apt install python3-venv -y
cd ~/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py


## Step 4.  Setup Frontend VM

sudo apt update && sudo apt install apache2 -y
sudo a2enmod proxy proxy_http
sudo cp frontend/apache-proxy.conf /etc/apache2/sites-available/000-default.conf
sudo cp frontend/index.html /var/www/html/index.html
sudo systemctl restart apache2
