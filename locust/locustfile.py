from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/de/mobilitaet/fahrzeuge-kontrollschilder/mofa-und-ebike.html")
        