## Aluno
- Henrique Camacho Farias
- 201711310031
## Compilador - LALG

- Projeto da disciplina de Compiladores 1

### Manual

- O arquivo main.py, dentro de compilador_7 dentro da pasta scripts, é o responsável por chamar os outros scripts para executar o compilador;
- As entradas estão na pasta `entradas` e, para mudar o arquivo de entrada para o teste, apenas é necessário manipular a variável ARQ, dentro do script main.py;
- Para ajudar na avaliação, foram disponibilizados 6 arquivos de teste, sendo os arquivos `entrada5.txt` e `entrada6.txt` os arquivos que estão "corretos";
- Os arquivos `entrada1.txt`, `entrada2.txt`, `entrada3.txt` e `entrada4.txt` são referentes a cada 1 dos 4 erros de análise semântica implementados; 
- `entrada1.txt` apresento o erro warning, quando uma variável é declarada mas não é utilizada(nenhuma atribuição, operação, função sobre ela como write/read ou dentro de um loop/condicional), `entrada2.txt` apresenta o erro de variável com nome repetido, `entrada3.txt` erro de variável não declarada e `entrada4.txt` erro quando, na declaração de variável, o usuário escolhe como nome do identificador uma palavra reservada da linguagem.
- Execute-o com python3;
- Dentro da pasta `comp/scripts` , execute o comando :

  - `python3 main.py`

- O grafo explicando as regras, está na pasta `grafo`

#### Tecnologias

- Python 3

#### Adendos IMPORTANTE
- O compilador final está incompleto contando apenas com o analisador léxico, sintático e algumas regras de semântica. O gerador de código intermediário não foi implementado devido a imprevistos que ocorreram nessa fase final de semestre...;
- Nas regras gramaticais disponibilizadas pelo professor Rafael, a regra <dc_v> ->  <tipo_var> : <variaveis> conta com os 2 pontos, enquanto que no codigo de teste disponibilizado pelo mesmo, não há esses 2 pontos, apresentando erro caso tente rodar este arquivo de exemplo que está no Ava;
- Como explicado acima, o compilador em questão foi desenvolvido para a linguagem LALG, apresentando além das regras pedidas pelo professor no txt, "adições" como o uso de procedures por exemplo;
- No entanto, nenhuma regra semântica foi implementado para o compilador que reconhece procedures, fazendo apenas a análise léxica e sintática
- O compilador que reconhece procedures está em compilador_3 juntamente com seus 2 arquivos de entrada enquanto que o projeto "final"/"definitivo"(que não faz a implementação de procedures) está em compilador_7;
- Na implementação da análise léxica, não foi utilizado o conceito de autõmatos, no entanto, não foi utilizado nenhum regex ou biblioteca que faz a tokenização e afins;
