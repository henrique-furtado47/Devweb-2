const express = require("express");
const app = express();
app.use(express.json());

const produtos = [
  { id: 1, nome: "Notebook", preco: 3500, categoria: "informatica" },
  { id: 2, nome: "Mouse", preco: 120, categoria: "informatica" },
  { id: 3, nome: "Teclado", preco: 250, categoria: "informatica" },
];

app.get("/produtos/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const produto = produtos.find((p) => p.id === id);
  if (produto) {
    res.json(produto);
  } else {
    res.status(404).json({ erro: "Produto não encontrado" });
  }
});

app.get("/produtos", (req, res) => {
    const { min_preco, max_preco } = req.query;
    
    let resultado = produtos;
    
    // Filtrar por preço mínimo
    if (min_preco) {
        resultado = resultado.filter(p => p.preco >= parseFloat(min_preco));
    }
    
    // Filtrar por preço máximo
    if (max_preco) {
        resultado = resultado.filter(p => p.preco <= parseFloat(max_preco));
    }
    
    res.json({ produtos: resultado });
});

app.listen(3000, () => {
  console.log("Servidor rodando na porta 3000");
});
