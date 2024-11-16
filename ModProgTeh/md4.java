 import java.math.BigInteger;
 import java.math.*; 
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
		//d[2] = new DALSKAITLIS(args[4], args[5]);//te nav pēc parauga
	    /*System.out.println("hello 1="+d[0].x);
	    System.out.println("hello 2="+d[0].y);

*/
		for(DALSKAITLIS tmpD : d) tmpD.display();

//		if (d[0].isGreater(d[1])) {dSk = d[0]; d[0] = d[1]; d[1] = dSk; }
/* ja pirmā daļa ir lielāka par otro, tad
 * pirmais kļūst par otro un
 * otrias kļūst par pirmo skaitli
		d[0].divide(d[1]);*/
		/*d[1].add(d[0]);
		d[2].divide(d[1]);

		for(DALSKAITLIS tmpD : d) tmpD.display();
*/
		/*System.out.println(d[0].isEqual(d[1]));
		System.out.println(d[1].isEqual(d[2]));
		System.out.println(d[2].isEqual(d[0]));*/
		
		//System.out.println(d[0].isGreater(d[1]));
		//System.out.println(d[1].isGreater(d[2]));
		//System.out.println(d[2].isGreater(d[0]));

		//System.out.println(d[2].isEqual(d[2]));
		//d[0].add(d[1]);
		d[0].divide(d[1]);

		} 
	void add( DALSKAITLIS d ) {
		System.out.println("add?");
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
       	String tmp3x="";
    	String tmp3y="";
    	int n=0;
    	BigInteger Ax, Ay, Bx, By, C, D1, D2, D,G;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res1[]; 
    	BigInteger res2[];
    	//if negatīvi, tad mīnusi augšā
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	//System.out.println("sigval1="+sigvalue1);
    	//System.out.println("sigval2="+sigvalue2);
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));
    	//vienado saucejus
    	C=Ay.multiply(By);
    	D1=Ax.multiply(By);
    	D2=Bx.multiply(Ay);
    	D=D1.add(D2); 
    	/*System.out.println("D="+D);
    	System.out.println("/");
    	System.out.println("C="+C);

    	System.out.println("D="+D);
    	System.out.println("/");
    	System.out.println("C="+C);*/
    	//izvelk veselo dalu
    	BigInteger res[]; 
    	res = D.divideAndRemainder(C);
    	//System.out.println("res1 0="+res[0]);
    	//System.out.println("res1 1="+res[1]);
    	int sigvalue = res[0].signum();
    	//System.out.println("sigvalue="+sigvalue);
    	if (sigvalue ==0 )//nav veselie
    	{    	
    		//saīsina
    		G=D.gcd(C);
    		D=D.divide(G);
    		C=C.divide(G);
    	   	tmp3x=D.toString();
        	tmp3y=C.toString();
    	}
    	else //ir veselie
    	{
    		/*
        		
    		if (Ay.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp2x=tmp2x+"_";
    			    	tmp2x=tmp2x+Ax.toString();
    			    	tmp2y=Ay.toString();
    		}*/
 
    		tmp3x=res[0].toString(); //+"_";//veselie
    		D=D.subtract(C.multiply(res[0]));
      		//mīnuss ir tikai pie veselā
    		D=D.multiply(BigInteger.valueOf(sigvalue));
    		//saīsina
    		G=D.gcd(C);
    		D=D.divide(G);
    		C=C.divide(G);
    		if (C.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp3x=tmp3x+"_";
    			    	tmp3x=tmp3x+D.toString();
    			    	tmp3y=C.toString();
    		}

    		    			
    	}
    	//izdruka

    	if (C.compareTo(BigInteger.valueOf(1))==0) {
        	System.out.println(tmp3x);
    	}
    	else {
    	System.out.print(tmp3x);
    	System.out.print("/");
    	System.out.println(tmp3y);
    	}
	
	}
	void divide( DALSKAITLIS d) {
		System.out.println("divide?");
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
       	String tmp3x="";
    	String tmp3y="";
    	int n=0;
    	BigInteger Ax, Ay, Bx, By, C, D1, D2, D,G;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res[]; 
    	D=Ax.multiply(By);
    	C=Ay.multiply(Bx);
    	//ja neg apakša
    	int sigvalue = C.signum();
//    	int sigvalue2 = By.signum();
    	D=D.multiply(BigInteger.valueOf(sigvalue));
    	C=C.multiply(BigInteger.valueOf(sigvalue));
    	
    	/*System.out.println("D="+D);
    	System.out.println("/");
    	System.out.println("C="+C);*/

    	//izvelk veselo dalu
    	//BigInteger res[]; 
    	res = D.divideAndRemainder(C);
    	//System.out.println("res1 0="+res[0]);
    	//System.out.println("res1 1="+res[1]);
    	sigvalue = res[0].signum();
    	//System.out.println("sigvalue="+sigvalue);
    	if (sigvalue ==0 )//nav veselie
    	{    	
    		//saīsina
    		G=D.gcd(C);
    		D=D.divide(G);
    		C=C.divide(G);
    	   	tmp3x=D.toString();
        	tmp3y=C.toString();
    	}
    	else //ir veselie
    	{
    		/*
        		
    		if (Ay.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp2x=tmp2x+"_";
    			    	tmp2x=tmp2x+Ax.toString();
    			    	tmp2y=Ay.toString();
    		}*/
 
    		tmp3x=res[0].toString(); //+"_";//veselie
    		D=D.subtract(C.multiply(res[0]));
      		//mīnuss ir tikai pie veselā
    		D=D.multiply(BigInteger.valueOf(sigvalue));
    		//saīsina
    		G=D.gcd(C);
    		D=D.divide(G);
    		C=C.divide(G);
    		if (C.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp3x=tmp3x+"_";
    			    	tmp3x=tmp3x+D.toString();
    			    	tmp3y=C.toString();
    		}

    		    			
    	}
    	//izdruka

    	if (C.compareTo(BigInteger.valueOf(1))==0) {
        	System.out.println(tmp3x);
    	}
    	else {
    	System.out.print(tmp3x);
    	System.out.print("/");
    	System.out.println(tmp3y);
    	}
    	
	}
	boolean isEqual(DALSKAITLIS d) { 
		System.out.println("isEqual?");
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	
    	BigInteger Ax, Ay, Bx, By, C, D;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res1[]; 
    	BigInteger res2[];
    	//if negatīvi, tad mīnusi augšā
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	//System.out.println("sigval1="+sigvalue1);
    	//System.out.println("sigval2="+sigvalue2);
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));

    	res1 = Ax.divideAndRemainder(Ay);
    	res2 = Bx.divideAndRemainder(By);
    	/*System.out.println("res1 0="+res1[0]);
    	System.out.println("res1 1="+res1[1]);
    	System.out.println("res2 0="+res2[0]);
    	System.out.println("res2 1="+res2[1]);*/
    	if(res1[0].compareTo(res2[0])==0){//sakrīt veselie
    		//System.out.println("EPirmaisIF return true");    		
    		if(res1[1].compareTo(res2[1])==0){//sakrīt atlikumi
    			//System.out.println("res1return true");
    			return true;
			}
    		else {	
    			//System.out.println("return false");
    			return false;
    		}
    		//return true;
    	}
    	else {	
    			//System.out.println("return false");
    			return false;
    	}    	
}
	boolean isGreater(DALSKAITLIS d) { 
		System.out.println("isGreater?");
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	
    	BigInteger Ax, Ay, Bx, By, C, D;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	Bx  = new BigInteger(tmp2x);
    	By = new BigInteger(tmp2y);
    	BigInteger res1[]; 
    	BigInteger res2[]; 
    	//ja apaksa negatīva, tad mīnusi dodas augšā
    	int sigvalue1 = Ay.signum();
    	int sigvalue2 = By.signum();
    	//System.out.println("sigval1="+sigvalue1);
    	//System.out.println("sigval2="+sigvalue2);
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue1));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue1));
    	Bx=Bx.multiply(BigInteger.valueOf(sigvalue2));
    	By=By.multiply(BigInteger.valueOf(sigvalue2));    	
    	res1 = Ax.divideAndRemainder(Ay);
    	res2 = Bx.divideAndRemainder(By);
    	/*System.out.println("res10= "+res1[0]);
    	System.out.println("res11= "+res1[1]);
    	System.out.println("res20= "+res2[0]);
    	System.out.println("res21= "+res2[1]);*/
    	if(res1[0].compareTo(res2[0])==1){//ja vesela dala ir lielāks
    		//System.out.println("Pirmais IF return true");
    		return true;
    	}
    	else if(res1[0].compareTo(res2[0])==0) {//ja vesela dala sakrit
    		//System.out.println("Pirmais ELSEIF");
    		if(res1[1].compareTo(res2[1])==1)//ja atlikums ir lielaks
    			{
    			//System.out.println("return true");
    			return true;}
    		else {	
    			//System.out.println("return false");
    			return false;
    		}

    		}
    	else {	
    		//System.out.println("return false");
    			return false;
    	}
    	
		}


	public void display() { 
		System.out.println("Display this!");
	//	System.out.println("skait="+x);
		//System.out.println("sauc="+y);
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x="";
    	String tmp2y="";
    	BigInteger Ax, Ay, B,C, D, E, F, G;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	B = new BigInteger("0");
    	C = new BigInteger("0");
       	D = new BigInteger("0");   	
    	E = BigInteger.valueOf(1);
    	F =new BigInteger("0");    	
    	//ja saucejs ir negativs
    	int sigvalue = Ay.signum();
    	Ax=Ax.multiply(BigInteger.valueOf(sigvalue));
    	Ay=Ay.multiply(BigInteger.valueOf(sigvalue));
    	BigInteger res[]; 
    	res = Ax.divideAndRemainder(Ay); 	
    	int sigvalue2 = res[0].signum();
    	//System.out.println("sigvalue="+sigvalue);
    	
    	if (sigvalue2 ==0 )//nav veselie
    	{ 
    		//saīsina
    		G=Ax.gcd(Ay);
    		Ax=Ax.divide(G);
        	Ay=Ay.divide(G);
    	   	tmp2x=Ax.toString();
        	tmp2y=Ay.toString();
    	}
    	else //ir veselie
    	{
    		tmp2x=res[0].toString(); //+"_";//veselie
    		Ax=Ax.subtract(Ay.multiply(res[0]));//samazina skaitītāju
    		//mīnuss ir tikai pie veselā
    		Ax=Ax.multiply(BigInteger.valueOf(sigvalue2));
    		//saīsina
    		G=Ax.gcd(Ay);
    		Ax=Ax.divide(G);
        	Ay=Ay.divide(G);
    		
    		if (Ay.compareTo(BigInteger.valueOf(1))!=0) {/// saucējs nav 1
    					tmp2x=tmp2x+"_";
    			    	tmp2x=tmp2x+Ax.toString();
    			    	tmp2y=Ay.toString();
    		}
    		    			
    	}  	
    	//izdruka
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
