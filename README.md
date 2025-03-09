# Docker Multi-Container Setup (PHP, Python, MySQL, Adminer, Nginx)

This project sets up a **multi-container environment** using **Docker Compose** for running PHP, Python, MySQL, Adminer, and Nginx. The containers are configured to share a **single MySQL database** and use Nginx as a reverse proxy.

## **Project Structure**

```
.
├── docker-compose.yml
├── nginx/
│   ├── conf.d/
│   │   ├── default.conf
├── php/
│   ├── Dockerfile
│   ├── src/
├── python/
│   ├── Dockerfile
│   ├── app.py
├── mysql/
│   ├── data/
│   ├── init.sql
├── adminer/
├── .env
└── README.md
```

---

## **1. Prerequisites**

Ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## **2. Setup & Configuration**

### **Step 1: Clone the Repository**

```sh
git clone https://github.com/your-repo/multi-container-docker.git
cd multi-container-docker
```

### **Step 2: Set Environment Variables**

Create a `.env` file and configure MySQL credentials:

```sh
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=mydatabase
MYSQL_USER=user
MYSQL_PASSWORD=password
```

---

## **3. Running the Containers**

Run the following command to build and start the services:

```sh
docker-compose up --build -d
```

To check running containers:

```sh
docker ps
```

To stop the containers:

```sh
docker-compose down
```

---

## **4. Accessing Services**

- **PHP Application**: [http://local.one](http://php.one)
- **Python Application**: [http://python.one](http://python.one)
- **Adminer (MySQL GUI)**: [http://adminer.one](http://adminer.one)

To test MySQL connection:

```sh
docker exec -it mysql_container mysql -uuser -ppassword mydatabase
```

---

## **5. Troubleshooting**

### **1. Nginx Shows "502 Bad Gateway"?**

Run the following:

```sh
docker logs nginx_container
```

If you see **"Connection refused"**, check if the service is running:

```sh
docker ps
```

Then, restart the containers:

```sh
docker-compose restart
```

### **2. Adminer Not Accessible via Nginx?**

Check if Adminer is listening on the correct port:

```sh
docker exec -it adminer_container sh -c "netstat -tlnp"
```

Ensure Adminer is accessible from Nginx:

```sh
docker exec -it nginx_container curl -I http://adminer_container:8080
```

If needed, reconnect Adminer to the network:

```sh
docker network connect app_network adminer_container
```

### **3. MySQL Connection Issues?**

Check MySQL logs:

```sh
docker logs mysql_container
```

Ensure the database is accessible inside a container:

```sh
docker exec -it php_container mysql -h mysql_container -uuser -ppassword mydatabase
```

---

## **6. Stopping & Cleaning Up**

To stop all containers:

```sh
docker-compose down
```

To remove all containers and networks:

```sh
docker-compose down --volumes --remove-orphans
```

---

## **7. Extending the Setup**

- Add **additional services** (Redis, Node.js, etc.).
- Configure **SSL/TLS** using Let's Encrypt.
- Implement **Docker Swarm** or **Kubernetes** for scalability.

---

## **8. License**

This project is licensed under the **MIT License**.

