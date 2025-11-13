# Identifier – Validador de Identificadores

### 1. Descrição do Problema

1.1 O objetivo do Identifier é verificar se uma string é um identificador válido. 

Um identificador é considerado válido quando:

- Começa com uma letra (```a-z``` ou ```A-Z```);
- Contém apenas letras e dígitos (```a-z```, ```A-Z```, ```0-9```);
- Possui de 1 a 6 caracteres de comprimento (inclusive).

A função retorna um valor booleano (```True``` ou ```False```) indicando se o identificador é válido.


### 2. Implementação

O programa foi implementado no arquivo ```identifier.py```, com a classe ```Identifier``` e o método ```validate_identifier()```, que realiza todas as verificações necessárias.

Os testes automatizados estão no arquivo ```test_identifier.py```, desenvolvidos com pytest.


### 3. Classes de Equivalência

| Critério | Classes Válidas | Classes Inválidas |
|:---------:|:---------------:|:----------------:|
| **Comprimento** | 1 a 6 caracteres | 0 caracteres ou mais de 6 caracteres |
| **Caractere inicial** | Letra (a-z, A-Z) | Dígito (0-9) ou símbolo (_, #, etc.) |
| **Demais caracteres** | Letras ou dígitos | Símbolos, espaços ou caracteres especiais |


### 3.1. Análise de Valor Limite

| Regra               | Valor Limite Inferior | Valor Limite Superior |
|--------------------|---------------------|---------------------|
| **Comprimento mínimo** | 0 → 1              | -                   |
| **Comprimento máximo** | -                  | 6 → 7               |
| **Caractere inicial**  | símbolo → letra    | letra → dígito      |

Esses limites foram usados para criar casos de teste que cobrem valores válidos e inválidos nas fronteiras das regras.


### 4. Tabela de Casos de Teste

| ID    | Entrada   | Classe de Equivalência                              | Análise de Valor Limite                     | Resultado Esperado |
|-------|-----------|----------------------------------------------------|--------------------------------------------|------------------|
| CT01  | ""        | Comprimento inválido (0 caracteres)               | Limite inferior (abaixo do mínimo)        | Inválido         |
| CT02  | "a"       | Comprimento mínimo válido / começa com letra      | Limite inferior válido                      | Válido           |
| CT03  | "abc"     | Comprimento dentro do intervalo válido / só letras | -                                         | Válido           |
| CT04  | "a1b2"    | Mistura de letras e dígitos válidos              | -                                          | Válido           |
| CT05  | "A12345"  | Letra maiúscula inicial / tamanho máximo         | Limite superior válido                      | Válido           |
| CT06  | "abc123"  | Letras e números até 6 caracteres                | Limite superior válido                      | Válido           |
| CT07  | "abcdefg" | Comprimento inválido (>6)                         | Limite superior excedido                    | Inválido         |
| CT08  | "abc1234" | Comprimento inválido (>6)                         | Limite superior excedido                    | Inválido         |
| CT09  | "1abc"    | Inicia com número                                 | Classe inválida (caractere inicial)        | Inválido         |
| CT10  | "2foo"    | Inicia com número                                 | Classe inválida (caractere inicial)        | Inválido         |
| CT11  | "9x9x9x"  | Inicia com número                                 | Classe inválida (caractere inicial)        | Inválido         |
| CT12  | "a_123"   | Contém símbolo não permitido                      | Classe inválida (caractere não alfanumérico)| Inválido        |
| CT13  | "123456"  | Somente dígitos (sem letra inicial)              | Classe inválida (caractere inicial)        | Inválido         |
| CT14  | "987654"  | Somente dígitos                                   | Classe inválida                             | Inválido         |
| CT15  | "0"       | Um dígito apenas                                  | Limite inferior inválido                     | Inválido         |
| CT16  | "a1b2c3"  | Letras e dígitos válidos (tamanho 6)             | Limite superior válido                      | Válido           |

### 5. Como Executar os Testes Localmente

5.1 Instale as dependências:

terminal: ```pip install pytest```

5.2 Execute os testes:

terminal: ````python -m pytest -v````

5.3 Saída Esperada:

<img width="1185" height="257" alt="image" src="https://github.com/user-attachments/assets/07dacdd9-823b-4582-8103-138ff7d5a9c8" />
