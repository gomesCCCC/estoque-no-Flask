- Estoque no Flask
Antes de seguir pelo caminho da IA, eu queria fazer um teste em um framework diferente e escolhi o Flask para colocar tudo o que eu estudei em prática. Como eu já desenvolvia em Java com Spring Boot, seria mais fácil aprender a sintaxe por causa das semelhanças e do conceito de API.
Portanto, como eu estava pensando em algo que me “forçaria” a aplicar toda a base de Python, pensei que um pequeno sistema de estoque seria interessante para desenvolver esses conceitos, que, de certa forma, foram bem aplicados, sendo resultado de um estudo de 30 dias em cima da linguagem.
Sobre o código em si, queria que todas as partes aplicassem pelo menos um conceito diferente, seguindo esta lógica:
- POO — Classe Produto e importação do Flask
Eu não me importei com a quantidade de atributos e métodos, e sim com o desempenho no projeto. Por isso, coloquei somente 6 atributos e 1 método, que executa o cadastro pelo cadastrar(), que referencia a API cadastrar_produto.
Tive cautela em classificar a tipagem de cada um dos respectivos atributos, certificando que tanto o método quanto o formulário sejam classificados como POST.
Há atributos que possuem características incomuns, como, por exemplo:
self.id
Tive um problema, pois sempre estive acostumado com o MySQL lidando com isso. A solução temporária que achei foi usar random.randint(000000,999999), que geraria um valor aleatório de 6 dígitos.
self.categoria
Fiz uma “gambiarra”, pois achei que seria interessante utilizar uma lista para comparar com a variável, em vez de ficar algo bagunçado, como vários objetos com “TV”, “TELEVISÃO”, “Televisao” — apesar de que isso poderia ser resolvido com lower().
  - Manipulação de documento — JSON
Como, nesse momento do estudo, eu não cheguei a desenvolver habilidade com pandas e a implementar o MySQL no Python, imaginei que seria o momento perfeito para colocar os dados com permanência em JSON.
Eu codifiquei duas funções:
abrir_arquivo()
Pega o estoque.json e o coloca em um dicionário. Não sei se foi necessário, mas coloquei um tratamento de erro caso o arquivo não existisse.
Tenho esse costume, pois geralmente não coloco um JSON predefinido na maioria dos meus códigos, o que faz dar FileNotFoundError, e sempre faço um return para isso não acontecer.
salvar_arquivo()
Eu só teria que colocar o estoque como parâmetro e usar json.dump, que guardaria esses dados.
Seguindo essa lógica, o sistema puxaria o JSON, criando uma “cópia” e referenciando um dicionário, como, por exemplo, o estoque. Usa append() em um segundo dicionário que compõe os atributos do novo produto e retorna esse mesmo para o salvar_arquivo(), reescrevendo o JSON por outro atualizado.
- Tratamento e validação de erros
Aqui não tem muito segredo: só tomei o cuidado de aplicar a devida classificação de tipagem usando raise ValueError, o que é simples, mas necessário nesse tipo de programa.
Para funcionar, só precisaria aplicar um pequeno código no HTML que retornaria onde deu errado.
  - Frontend e próximos ajustes
Por fim, fiz um pequeno frontend para não deixar com um aspecto cru de só usar o terminal — HTML e CSS não são minha praia, então não me julgue ;-;.
Tem alguns problemas de lógica, como, por exemplo, o random.randint, que pode gerar, em algum momento, um ID repetido. Mas são questões que pretendo organizar aos poucos durante os estudos.
Porém, considero um ótimo início vindo de quem está aprendendo Python há 30 dias.

- 
