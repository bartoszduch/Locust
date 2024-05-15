from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def convert_temp(self):
        self.client.get("/convert?fahrenheit=100")
