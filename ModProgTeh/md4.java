import java.math.BigInteger;
public class DALSKAITLIS {
	  String x;
	  String y;
	  public DALSKAITLIS(String sk) {
		    x=sk;
		    y="1";
		  }
	  public DALSKAITLIS(String skait, String sauc) {
	    x=skait;
	    y=sauc;
	  }
	public static void main(String[] args) {
		DALSKAITLIS dSk;
		DALSKAITLIS d[] = new DALSKAITLIS[3];

		d[0] = new DALSKAITLIS(args[0], args[1]);
		d[1] = new DALSKAITLIS(args[2], args[3]);
		d[2] = new DALSKAITLIS(args[4]);

		for(DALSKAITLIS tmpD : d) tmpD.display();

		if (d[0].isGreater(d[1])) {dSk = d[0]; d[0] = d[1]; d[1] = dSk; }

		d[0].divide(d[1]);
		d[1].add(d[0]);
		d[2].divide(d[1]);

		for(DALSKAITLIS tmpD : d) tmpD.display();

		System.out.println(d[0].isEqual(d[1]));
		System.out.println(d[1].isEqual(d[2]));
		System.out.println(d[2].isEqual(d[2])); 

		} 
	void add( DALSKAITLIS d ) {
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	BigInteger Ax, Ay, Bx, By, C, D1, D2, D;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));
    	C=Ay.multiply(By);
    	D1=Ax.multiply(By);
    	D2=Bx.multiply(Ay);
    	D=D1.add(D2); 
    	this.x=D.toString();
    	this.y=C.toString();	
	}
	void divide( DALSKAITLIS d) {
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	BigInteger Ax, Ay, Bx, By, C,D;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	D=Ax.multiply(By);
    	C=Ay.multiply(Bx);
    	int sigvalue = C.signum();
    	D=D.multiply(BigInteger.valueOf(sigvalue));
    	C=C.multiply(BigInteger.valueOf(sigvalue));
    	this.x=D.toString();
    	this.y=C.toString();
	}
	boolean isEqual(DALSKAITLIS d) { 
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;    	
    	BigInteger Ax, Ay, Bx, By;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res1[]; 
    	BigInteger res2[];
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));
    	res1 = Ax.divideAndRemainder(Ay);
    	res2 = Bx.divideAndRemainder(By);
    	if(res1[0].compareTo(res2[0])==0){//sakrīt veselie
       		if(res1[1].compareTo(res2[1])==0){//sakrīt atlikumi
    			return true;
			}
    		else {	
    			return false;
    		}
    	}
    	else {	
    			return false;
    	}    	
	}
	boolean isGreater(DALSKAITLIS d) { 
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	
    	BigInteger Ax, Ay, Bx, By;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res1[]; 
    	BigInteger res2[]; 
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));    	
    	res1 = Ax.divideAndRemainder(Ay);
    	res2 = Bx.divideAndRemainder(By);
    	if(res1[0].compareTo(res2[0])==1){//ja vesela dala ir lielāks
    		return true;
    	}
    	else if(res1[0].compareTo(res2[0])==0) {//ja vesela dala sakrit
    		if(res1[1].compareTo(res2[1])==1)//ja atlikums ir lielaks
    			{
    			return true;}
    		else {	
    			return false;
    		}
    	}
    	else {	
    		return false;
    	}    	
	}
	public void display() { 
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x="";
    	String tmp2y="";
    	BigInteger Ax, Ay, G;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	int sigvalue = Ay.signum();
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue));
    	BigInteger res[]; 
    	res = Ax.divideAndRemainder(Ay); 	
    	int sigvalue2 = res[0].signum();
    	if (sigvalue2 ==0 ){ 
    		G=Ax.gcd(Ay);
    		Ax=Ax.divide(G);
        	Ay=Ay.divide(G);
    	   	tmp2x=Ax.toString();
        	tmp2y=Ay.toString();
    	}
    	else{
    		tmp2x=res[0].toString(); //+"_";//veselie
    		Ax=Ax.subtract(Ay.multiply(res[0]));//samazina skaitītāju
    		Ax=Ax.multiply(BigInteger.valueOf(sigvalue2));
    		G=Ax.gcd(Ay);
    		Ax=Ax.divide(G);
        	Ay=Ay.divide(G);    		
    		if (Ay.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp2x=tmp2x+"_";
    			    	tmp2x=tmp2x+Ax.toString();
    			    	tmp2y=Ay.toString();
    		}    		    			
    	}      	//izdruka
    	if (Ay.compareTo(BigInteger.valueOf(1))==0) {
        	System.out.println(tmp2x);
    	}
    	else {
    	System.out.print(tmp2x);
    	System.out.print("/");
    	System.out.println(tmp2y);
    	}  		
	}

}
