# π [5430λ² : AC](https://www.acmicpc.net/problem/5430)
- π λ¬Έμ  μ ν : κ΅¬ν
- π λ¬Έμ  λ±κΈ : GOLD 5
  <br/><br/>

# π λ¬Έμ  μ‘°κ±΄

|μκ° μ ν|λ©λͺ¨λ¦¬ μ ν|
|:------:|:---:|
|1 μ΄|256 MB|
<br/>

# π λ¬Έμ 
<div style="font-size: 17px">
μ μμ΄λ μ£Όλ§μ ν  μΌμ΄ μμ΄μ μλ‘μ΄ μΈμ΄ ACλ₯Ό λ§λ€μλ€. ACλ μ μ λ°°μ΄μ μ°μ°μ νκΈ° μν΄ λ§λ  μΈμ΄μ΄λ€.
μ΄ μΈμ΄μλ λ κ°μ§ ν¨μ R(λ€μ§κΈ°)κ³Ό D(λ²λ¦¬κΈ°)κ° μλ€.

ν¨μ Rμ λ°°μ΄μ μλ μ«μμ μμλ₯Ό λ€μ§λ ν¨μμ΄κ³ , Dλ μ²« λ²μ§Έ μ«μλ₯Ό λ²λ¦¬λ ν¨μμ΄λ€.
λ°°μ΄μ΄ λΉμ΄μλλ° Dλ₯Ό μ¬μ©ν κ²½μ°μλ μλ¬κ° λ°μνλ€.

ν¨μλ μ‘°ν©ν΄μ ν λ²μ μ¬μ©ν  μ μλ€. μλ₯Ό λ€μ΄, "AB"λ Aλ₯Ό μνν λ€μμ λ°λ‘ μ΄μ΄μ Bλ₯Ό μννλ ν¨μμ΄λ€.
μλ₯Ό λ€μ΄, "RDD"λ λ°°μ΄μ λ€μ§μ λ€μ μ²μ λ μ«μλ₯Ό λ²λ¦¬λ ν¨μμ΄λ€.

λ°°μ΄μ μ΄κΈ°κ°κ³Ό μνν  ν¨μκ° μ£Όμ΄μ‘μ λ, μ΅μ’ κ²°κ³Όλ₯Ό κ΅¬νλ νλ‘κ·Έλ¨μ μμ±νμμ€.
</div>
<br/>

# π μλ ₯
<div style="font-size: 17px">
μ²«μ§Έ μ€μ νμ€νΈ μΌμ΄μ€μ κ°μ Tκ° μ£Όμ΄μ§λ€. Tλ μ΅λ 100μ΄λ€.

κ° νμ€νΈ μΌμ΄μ€μ μ²«μ§Έ μ€μλ μνν  ν¨μ pκ° μ£Όμ΄μ§λ€. pμ κΈΈμ΄λ 1λ³΄λ€ ν¬κ±°λ κ°κ³ , 100,000λ³΄λ€ μκ±°λ κ°λ€.

λ€μ μ€μλ λ°°μ΄μ λ€μ΄μλ μμ κ°μ nμ΄ μ£Όμ΄μ§λ€. (0 β€ n β€ 100,000)

λ€μ μ€μλ [x1,...,xn]κ³Ό κ°μ ννλ‘ λ°°μ΄μ λ€μ΄μλ μκ° μ£Όμ΄μ§λ€. (1 β€ xi β€ 100)

μ μ²΄ νμ€νΈ μΌμ΄μ€μ μ£Όμ΄μ§λ pμ κΈΈμ΄μ ν©κ³Ό nμ ν©μ 70λ§μ λμ§ μλλ€.
</div>
<br/>

# π μΆλ ₯
<div style="font-size: 17px">
κ° νμ€νΈ μΌμ΄μ€μ λν΄μ, μλ ₯μΌλ‘ μ£Όμ΄μ§ μ μ λ°°μ΄μ ν¨μλ₯Ό μνν κ²°κ³Όλ₯Ό μΆλ ₯νλ€. λ§μ½, μλ¬κ° λ°μν κ²½μ°μλ errorλ₯Ό μΆλ ₯νλ€.
</div>

## π μμΆλ ₯ μμ1
### μλ ₯ 
    4
    RDD
    4
    [1,2,3,4]
    DD
    1
    [42]
    RRD
    6
    [1,1,2,3,5,8]
    D
    0
    []

### μΆλ ₯
    [2,1]
    error
    [1,2,3,5,8]
    error
