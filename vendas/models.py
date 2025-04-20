from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
      return self.nome
    
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    
    
   
    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    Cliente = models.ForeignKey(Cliente ,on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
     return f"{self.Cliente}"
 
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

   
    class Meta:
     verbose_name='cliente'
     verbose_name ='produto'   
     verbose_name='venda' 
     verbose_name='itemvenda'
