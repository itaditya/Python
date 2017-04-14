import subprocess
class Example():

    def __init__(self):
        self.fileName = "test.html"
        self.project = {"location" : "F:/testing"}

    def create(self):
        print("----")
        # subprocess.Popen(
        #     ['touch',self.fileName], cwd=self.project["location"])
        subprocess.call('echo abcd > test.html', shell=True,cwd=self.project["location"])
        subprocess.Popen(
            ['subl', self.project["location"]])

def main():
    app = Example()
    app.create()


if __name__ == '__main__':
    main()
