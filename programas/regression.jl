using Plots
using Distributions
using Random

Random.seed!(1234)

T = 5
var_foo = rand(Uniform(0,10))
pontosX = Float64[]
pontosY = Float64[]

function f(x,erro)
    var_foo*x+erro
end


for i in 1:10
    xi = rand(Uniform(-T, T))
    e = randn() #erro
    push!(pontosX, xi)
    push!(pontosY, f(xi,e))
end

function estimar_coeficiente(x,y)
    tamanho = size(x,1)
    media_x = mean(x)
    media_y = mean(y)
    #Calculando o desavio
    desvio_xy = sum(x .* y) - media_x*media_y*tamanho
    desvio_xx = sum((x .* x)) - (media_x^2)*tamanho
    coef_Reg = desvio_xy / desvio_xx
    ajuste = media_y - media_x*coef_Reg
    return ajuste, coef_Reg
end


a,b = estimar_coeficiente(pontosX,pontosY)
plot([-5,5] , [-a*5+b,a*5+b], label=["regressão"])
plot!(pontosX, pontosY, seriestype=:scatter)