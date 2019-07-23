class userCusine():
    def get(self):
        all=self.request.get_all('cusine')
        if not all:
            self.response.out.write('sss')
            return self.response.out.write(all)

print userCusine()
