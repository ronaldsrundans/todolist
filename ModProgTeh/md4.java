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
		d[2] = new DALSKAITLIS(args[4], args[5]);
	    /*System.out.println("hello 1="+d[0].x);
	    System.out.println("hello 2="+d[0].y);*/


		for(DALSKAITLIS tmpD : d) tmpD.display();
/*
		if (d[0].isGreater(d[1])) {dSk = d[0]; d[0] = d[1]; d[1] = dSk; }

		d[0].divide(d[1]);
		d[1].add(d[0]);
		d[2].divide(d[1]);

		for(DALSKAITLIS tmpD : d) tmpD.display();

		System.out.println(d[0].isEqual(d[1]));
		System.out.println(d[1].isEqual(d[2]));
		System.out.println(d[2].isEqual(d[2]));*/
		} 
	void add( DALSKAITLIS d ) {
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x=d.x;
    	String tmp2y=d.y;
    	BigInteger Ax, Ay, C, D;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
	}
	void divide( DALSKAITLIS d) {}
	boolean isEqual(DALSKAITLIS d) { 
		return false;
		}
	boolean isGreater(DALSKAITLIS d) { 
		return false;
		}
	public void display() { 
		//3/4 jāizvada kā 3/4, 12/34 vietā jāizvada 6/17, 
		//-18/3 vietā jāizvada -6, 34/12 vietā jāizvada 2_5/6, 
		//-7/-4 vietā jāizvada 1_3/4, -1/-2 vietā jāizvada 1/2, 
		//1/-2 vietā jāizvada -1/2;
		System.out.println("Display this!");
		System.out.println("skait="+x);
		System.out.println("sauc="+y);
    	String tmp1x=this.x;
    	String tmp1y=this.y;
    	String tmp2x="";
    	String tmp2y="";
    	String veseli;
    	int n=0, negx=0, negy=0, neg=0;
    	//int		ves=0; ///Izdzēst pārveido par BigInt
    	BigInteger Ax, Ay, B,C, D, E, F;
    	Ax  = new BigInteger(tmp1x);
    	Ay = new BigInteger(tmp1y);
    	B = new BigInteger("0");
    	C = new BigInteger("0");
    
    	D = new BigInteger("0");   	
    	E = BigInteger.valueOf(1);
    	F =new BigInteger("0");
    	
    	int sigvalue = Ax.signum();
    	int sigvalue2;
    	if(sigvalue<0) {
    		//System.out.println("neg tmp2x"+sigvalue);
    		negx=1;
    		Ax=Ax.multiply(BigInteger.valueOf(-1));
    		//tmp2x=tmp2x.substring(1);
    	}
    	sigvalue = Ay.signum();
    	if(sigvalue<0) {
    		//System.out.println("neg tmp2y"+sigvalue);
    		negy=1;
    		Ay=Ay.multiply(BigInteger.valueOf(-1));
    		//tmp2y=tmp2y.substring(1);
    	}
    	
    	
    	
    	BigInteger res[]; 
    	res = Ax.divideAndRemainder(Ay);
    	//System.out.println("Quotient = " + res[0]+"\nRemainder = " + res[1]); 

    	sigvalue2 = res[0].signum();
 
    	if(sigvalue2!=0) {
    		Ax=res[1];
    	}

    	
    	D=Ax.gcd(Ay);
    	//System.out.println("GCD= "+D);
    	B=Ax.divide(D);
    	C=Ay.divide(D);
    	//F=Ax.divideAndRemainder(Ay);
    	//System.out.println("Bvalue= "+B);
    	//System.out.println("Cvalue= "+C);

    	tmp2x=B.toString();
    	tmp2y=C.toString();
    	//System.out.println("tmp2x="+tmp2x);
    	//System.out.println("tmp2y="+tmp2y);
    	

    	
    	
    	//System.out.println(tmp2y.getClass());
    	//System.out.println("this value="+tmp2y);
    	//if(y=="1") {
    	//System.out.println("tmp2= "+tmp2y);
    	//System.out.println("tmp2 len= "+tmp2y.length());
    	if(tmp2y.length()==1) {
    		n=Integer.parseInt(tmp2y.substring(0, tmp2y.length()));
    		}
        if(n==1 && tmp2y.length()==1) {

    		//System.out.println("Enter IF");
        	if(negx != negy) {
    			System.out.print("-");
    		}
        	/*if(ves>0) {
        		System.out.println(ves);

        	}*/
        	if (sigvalue2!=0) {
        		tmp2x=res[0].toString();
        		System.out.println(tmp2x);
        	}

    		//System.out.println("sauc ir 1"+tmp2x);
    		//System.out.println(tmp2x);
    	}
        else {
        	//System.out.println("Enter ELSE");
        	
        	
        	if(negx != negy) {
        		System.out.print("-");
        	}
        	//if(ves>0) {
        	if (sigvalue2!=0) {
        		
        		System.out.print(res[0].toString()+"_");

        	}

    		System.out.println(tmp2x+"/"+tmp2y);
    		//System.out.println(tmp2y);


        }

	}
	/*
///End with	 
	 16 -32 36 45 -2
///	 
	  3 4 
	  12 34 
	  -18 3 
	  34 12 
	  -7 -4 
	  -1 -2
	  1 -2
	  ///
	-1/2
4/5
-2
-5/8
7/40
-11_3/7
false
false
true*/



}
