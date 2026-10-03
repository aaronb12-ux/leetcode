class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for asteroid in asteroids:
         
            if not stack:
                stack.append(asteroid)

            elif stack[-1] > 0 and asteroid < 0: #moving towards each other 

                while True:
                 
                    top_stack = stack[-1]

                    if abs(asteroid) > top_stack:

                        if top_stack < 0:
                            stack.append(asteroid)
                            break
                    
                        stack.pop()

                        if not stack:
                            stack.append(asteroid)
                            break
                     
                        continue

                    if abs(asteroid) == top_stack and top_stack > 0:
                        stack.pop()
                     
                        break
                 
                    if top_stack > abs(asteroid):
                        break
            else:
                stack.append(asteroid)


        return stack
