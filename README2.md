<span style = 'font-family: Times New Roman; font-size: 20px;' >
    &emsp;&emsp;&emsp;<i>Logistic regression</i> adalah bentuk klasifikasi yang memprediksi data yang bersifat kategorikal/<i>binary</i>/diskrit,  <br>
    &emsp;&emsp;&emsp;seperti "<i>churn</i> atau <i>no churn</i>" dan "1 atau 0" untuk <i>binary class</i>; 'GOOD', 'BEST', 'NORMAL', <br>
    &emsp;&emsp;&emsp;'BAD', 'WORST' untuk <i>multiclass</i>; <i>etc</i> [4]. Ia dapat memprediksi probabilitas data antara 0 hingga 1<br>
    &emsp;&emsp;&emsp;dalam bentuk <i>sigmoid function</i> [4]. Data dengan probabilitas yang berada di atas <i>sigmoid function</i><br>
    &emsp;&emsp;&emsp;terkategori sebagai 1, sedangkan yang berada di bawahnya terkategori sebagai 0 [4]. Perbedaan dengan <i>linear<br> 
    &emsp;&emsp;&emsp;regression</i> adalah di mana <i>linear regression</i> hanya memprediksi data numerikal yang dilambangkan dengan<br>
    <center>$\bf \hat{y}  = \mathbf{\theta_0} + \mathbf{X}\mathbf{\theta}_{1:n-1}^T$</center><div style ='text-align:right'>(1)</div><br>
    <center>atau</center><br>
    <center>$\hat{y}  = \theta_0 + x_1\theta_1^{T}  + x_2\theta_2^{T}  + \dots + x_n\theta_{n-1}^{T} $</center><div style ='text-align:right'>(2)</div><br>
    &emsp;&emsp;&emsp;Di mana $\mathbf{\hat{y}} =
\begin{bmatrix}
\hat{y}_{0} \\
\hat{y}_{1} \\
\vdots\\
\hat{y}_{n-1}
\end{bmatrix}
$, $\mathbf{\theta_0} =  
\begin{bmatrix}
\theta_{0,0} \\
\theta_{0,1} \\
\vdots\\
\theta_{0,n-1}
\end{bmatrix}
$, 
     $\mathbf{\theta_1} = 
\begin{bmatrix}
\theta_{1,0} \\
\theta_{1,1} \\
\vdots\\
\theta_{1,n-1}
\end{bmatrix}$ , $\dots$, 
    $\mathbf{\theta_{n-1}} = 
    \begin{bmatrix}
\theta_{n-1,0} \\
\theta_{n-1,1} \\
\vdots\\
\theta_{n-1,n-1}
\end{bmatrix}
    $, <br>
    &emsp;&emsp;&emsp;dan 
     $\mathbf {X} = 
\begin{bmatrix}
x_{0,0} & x_{0,1} & \dots & x_{0,n-1} \\
x_{1,0} & x_{1,1} & \dots & x_{1,n-1}\\
\vdots\ & \vdots & \ddots & \vdots \\
x_{n-1,0} & x_{n-1,1} & \dots & x_{n-1,n-1} 
\end{bmatrix}$, dan $n$ merupakan dimensi dari fitur (variabel), di<br>
    &emsp;&emsp;&emsp;mana $\bf x_{1,:}$  merupakan nilai x pada atribut pertama, dan seterusnya. <br>
    &emsp;&emsp;&emsp;<i>Linear regression</i> berbentuk garis lurus pada dua dimensi dan berbentuk <i>plane</i> datar<br>
    &emsp;&emsp;&emsp;pada tiga dimensi [4]. Perlu diingat bahwa <b>persamaan (1)</b><br>
    &emsp;&emsp;&emsp;menghasilkan prediksi 1 dimensi, sedangkan <b>persamaan (2)</b> menghasilkan prediksi n$\times$1 dimensi. <br>
    &emsp;&emsp;&emsp;<b>Persamaan (1)</b> menggunakan variabel $\mathbf{\theta}$ dan $\mathbf{X}$ yang dicetak tebal, <br> &emsp;&emsp;&emsp;di mana <b>persamaan (2)</b> sebaliknya. Jika <i>linear regression</i> "dipaksakan" untuk <i>dependent variable</i> <br>
    &emsp;&emsp;&emsp;yang bersifat <i>categorical</i>, maka<br>
    <center>$\hat{y} = 
    \left\{
        \begin{array}{}
            1 \quad if \quad \mathbf{\theta}^T \mathbf{X} \geq 0.5 \\
            0 \quad if \quad \mathbf{\theta}^T \mathbf{X} < 0.5
        \end{array}
    \right.$</center><div style ='text-align:right'>(3)</div><br>
    &emsp;&emsp;&emsp;<b>Persamaan (3) </b>ini juga berlaku untuk <i>logistic regression</i> [4]. Dari persamaan ini dapat dilihat bahwa <i>classifier</i><br>
    &emsp;&emsp;&emsp;tidak dapat menentukan probabilitas dari nilai $\hat{y}$ jika $\geq 1$ dan jika <br>
    &emsp;&emsp;&emsp;$<$ 1. Di sinilah <i>logistic regression</i> berperan untuk mengatasi masalah ini [4].
    <br><br><br>
    &emsp;&emsp;&emsp;Berbeda dengan <i>logistic regression</i>, di mana grafiknya berbentuk <i>sigmoid</i> atau seperti huruf "S".<br>
    &emsp;&emsp;&emsp;Di samping <i>dependent variable</i> yang di-<i>train</i> bersifat diskrit/<i>binary</i>/<i>categorical</i>,<br>
    &emsp;&emsp;&emsp; probabilitas <i>dependent variable</i> yang di-<i>predict</i>/di-<i>test</i> harus bersifat <i>continue</i> yang berada di interval $[0,1]$ [4].<br>
    &emsp;&emsp;&emsp;Contoh aplikasi dari <i>logistic regression</i> adalah [4]
    <ul style= 'margin-left: 50px'>
        <li>memprediksi probabilitas seseorang terkena serangan jantung berdasarkan berat badan, konsumsi rokok, dan
            konsumsi alkohol selama periode tertentu;</li>
        <li>memprediksi probabilitas kematian pasien berdasarkan luka yang diderita;</li>
        <li>memprediksi apakah pasien diderita gejala penyakit tertentu berdasarkan <i>blood pressure</i>, kadar gula, dan berat badan;</li>
        <li>memprediksi apakah <i>customer</i> membeli suatu produk atau berhenti dari langganan internet;</li>
        <li>memprediksi apakah suatu sistem gagal atau berhasil berproses berdasarkan <i>current behavior</i>-nya</li>
        <li>memprediksi apakah pemilik rumah gagal atau berhasil membayar hipotek<br>
    </ul>
    &emsp;&emsp;&emsp;Rumus dari <i>sigmoid function</i> sendiri adalah sebagai berikut<br>
    &emsp;&emsp;&emsp;<center>$\sigma(\mathbf{\theta}^T \mathbf{X}) = \frac{1}{1+e^{-\mathbf{\theta}^T\mathbf{X}}}$</center><div style='text-align: right'>(4)</div>
</span>
