
@task(3)
def convert_temp(self):
    self.client.get("/convert?fahrenheit=100")
