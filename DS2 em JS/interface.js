let loop = true;

while (loop) {
  const ddd = parseInt(prompt("Digite o DDD: "));

  if (codigos.has(ddd)) {
    alert("a cidade de DDD" + ddd + " é " + codigos.get(ddd));
  } else {
    alert("DDD não cadastrado");
  }

  loop = confirm("Quer digitar outro código?");
}