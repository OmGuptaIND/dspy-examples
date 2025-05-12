from app.generator import ImageGenerator

def main():
    user_prompt = input("Enter Your Prompt: ")


    generator = ImageGenerator(user_prompt, 5)

    generator.generate()

if __name__ == "__main__":
    main()
