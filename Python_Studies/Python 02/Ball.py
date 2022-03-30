class Ball:

    def __init__(self, canvas, x, y, diameter, VelocityX, VelocityY, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y, diameter, diameter, fill=color)
        self.VelocityX = VelocityX
        self.VelocityY = VelocityY

    def move(self):
        coordinates = self.canvas.coords(self.image)
        # print(coordinates)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.VelocityX = -self.VelocityX
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.VelocityY = -self.VelocityY

        self.canvas.move(self.image, self.VelocityX, self.VelocityY)
