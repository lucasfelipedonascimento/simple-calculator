# Simple Calculator

## Português

- O projeto da calculadora simples foi desenvolvido para demonstração dos conhecimentos adquiridos no curso CS50 de Python. Apesar de ser simples, ele passa pela implementação e uso de funções personalizadas, operações aritméticas, validações condicionais, variáveis de armazenamento de valores, conversão de tipos de dados, entradas e saídas de dados para o usuário, testes unitários e variáveis de ambiente.
- No vídeo de apresentação, demonstrei ao vivo como a calculadora está funcionando.
  1.  Fiz a demonstração do usuário escolhendo a operação que deseja fazer.
  2.  Fiz a demonstração do usuário inserindo os números que deseja operar.
  3.  Fiz a demonstração do usuário visualizando o resultado da operação.
  4.  Também foi feita uma demonstração de como a conversão de dados da entrada do usuário para que os números funcionem realmente como número e não como string é feita.
  - Demonstrando inclusive que se o número não for convertido, o python vai entender ele como uma string, retornando um resultado inesperado do cálculo aguardado pelo usuário que está utilizando a calculadora, exemplo:
    - Se a conversão dos números **5** e **2** não forem feitas de **string** para **inteiro**, ao invés da soma **5** + **2** = **7**, o resultado será **52**, pois o python vai concatenar ao invés de somar os números.
  5. A demonstração dos testes unitários também foi feita usando o pytest e testando as funções da calculadora.

## English

- The simple calculator project was developed to demonstrate the knowledge acquired in the CS50 Python course. Despite its simplicity, it covers the implementation and use of custom functions, arithmetic operations, conditional validations, value storage variables, data type conversion, user input and output, unit tests, and environment variables.
- In the presentation video, I demonstrated live how the calculator is working.

1. I demonstrated the user choosing the operation they want to perform.
2. I demonstrated the user entering the numbers they want to operate on.
3. I demonstrated the user viewing the result of the operation.
4. A demonstration was also made of how the conversion of user input data so that the numbers actually function as numbers and not as strings is done.

- Demonstrating that if the number is not converted, Python will interpret it as a string, returning an unexpected result from the calculation expected by the user using the calculator, for example:
- If the conversion of the numbers **5** and **2** is not done from **string** to **integer**, instead of the sum **5** + **2** = **7**, the result will be **52**, because Python will concatenate instead of adding the numbers.

5. The unit tests were also demonstrated using pytest and testing the calculator functions.

## Video Presentation

[Video Presentation](https://youtu.be/lPMeRkUi-yY?si=4uJW_OD8ygZPU7JK)

# Step by Step

- 1. Create virtual environment in the project directory.
  ```bash
  python -m venv venv
  ```
- 2. Activate the virtual environment.
  ```bash
  source venv/bin/activate
  ```
- 3. Install the dependencies.
  ```bash
  pip install -r requirements.txt
  ```
- 4. Run the project.
  ```bash
  python project.py
  ```
- 5. Test the project.
  ```bash
  pytest test_project.py -s
  ```

# Test Cases

- Add: 1 + 2 = 3
- Subtract: 1 - 2 = -1
- Multiply: 1 \* 2 = 2
- Divide: 1 / 2 = 0.5
