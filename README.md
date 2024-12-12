## Introdução
Este repositório contém os materiais necessários para a execução da atividade prática do dia 11/12/2024 da disciplina optativa de Quantum Safe do Instituto de Tecnologia e Liderança (Inteli).

Nesse laboratório aprenderemos na prática como o Algoritmo de Shor pode impactar algoritmos de criptografia assimétrica. 


## Requisitos

### • Instalação - Qiskit
<p align="justify">
A biblioteca Qiskit, um projeto da IBM, é uma das soluções adotadas para o desenvolvimento das atividades dessa disciplina.

Para isso, crie uma conta na IBM Quantum Platform (https://quantum.ibm.com/). Instale a biblioteca seguindo os passos do seguinte link oficial (https://docs.quantum.ibm.com/guides/install-qiskit), ou, seguindo este vídeo (https://www.youtube.com/watch?v=dZWz4Gs_BuI). Você poderá simular a execução de algoritmos quânticos na sua própria máquina ou submetê-los para execução nos computadores quânticos disponibilizados pela IBM (para isso utilize o token de API disponibilizado na sua conta). Have fun!
</p>

### • Instalação - PyCryptoDome

Instale a biblioteca de criptografia através da linha da seguinte comando pip no seu ambiente:

```
pip install pycryptodome
```
## Breve Revisão RSA

Ser coprimo refere-se a um par de números que tem o maior divisor comum (MDC) igual a 1. Isso significa que esses números não compartilham nenhum divisor maior do que 1. 



## Ideia Principal do Ataque 

O módulo público _n_ é igual a um número primo _p_ vezes um número primo _q_. Se você conhece _p_ e _q_ (e _e_ da chave pública), poderá determinar a chave privada, quebrando assim a criptografia. No entanto, fatorar um _n_ grande para achar _p_ e _q_ é muito difícil sem o uso de um computador quântico eficiente. Um _n_ pequeno, talvez, possa ser fatorado através do Algoritmo de Shor em um computador quântico disponível agora. Vamos descobrir! 

A ideia básica do ataque consiste em fatorizar _n_ (que é público), dessa forma, o atacante pode derivar a chave privada (_d_) com _p_, _q_, e _e_ através da seguinte relação _d ≡ e^-1 mod Φ(n)_. Lembrando que _Φ(n)=(p-1)×(q-1)_. 

## Cenário Reduzido para Quebra

Para fins didáticos, cada primo _p_ e _q_ é gerado com 8 bits, conforme a chamada padrão da função generate_prime(bits=8).

O tamanho de _n_ será aproximadamente a soma dos tamanhos de _p_ e _q_.

A chave privada é composta por _n_ e _d_. O tamanho de _n_ determina o tamanho da chave RSA, que é de aproximadamente 16 bits nesse caso.
O valor de _d_ (o expoente da chave privada) é menos previsível em tamanho exato, mas geralmente será de um tamanho comparável ao de 
_𝜙(n)_ que é um pouco menos de 16 bits neste exemplo.

• Uma visão geral dos tamanhos de chaves RSA comumente usados:

1024 bits

2048 bits

3072 bits

4096 bits

## Fluxo da Dinâmica
![alice bob carlos drawio](https://github.com/user-attachments/assets/b656db96-39d7-4428-859f-ce014e5995da)

## Atividade

### • Análise do Programa Alice_Bob

Realize uma análise preliminar do programa em questão e responda as seguintes perguntas:

- Quais são as principais etapas do programa?
- Quais são os artefatos gerados?
- Quais são públicos e quais são privados? 

### • Mensagem Secreta

Junto com seu grupo, combinem uma frase secreta (sem caracteres especiais) que não deve ser compartilhada com nenhum outro grupo. 

![image](https://github.com/user-attachments/assets/950254f6-fac5-47fa-adc5-202e978a3cb4)

Substitua a frase padrão do trecho do código do programa Alice_Bob.py pela frase escolhida pelo grupo. 

### • Canal de Comunicação Simulado
Iremos utilizar um drive aberto para que cada grupo disponibilize os dados considerados públicos em uma comunicação:
#### https://drive.google.com/drive/folders/15dsGyEeDWbrR268lTc6S-Et531BGVeLy?usp=sharing
Crie uma pasta com o nome do seu grupo e dentro dela faça o upload da pasta "public" resultante da execução do programa "Alice_Bob". 
Acesse e copie a pasta "public" disponibilizada por cada grupo. 

### 
