public class prob009{
	public static void main(String[] args){
		int n = 1000;
		int ret = 0;
		int num = 0;
		for( int a=1 ; a<=n/3 ; a++ ){
			for( int b=a+1 ; b<=n/2 ; b++ ){
				for( int c=b+1 ; c<=n ; c++ ){
					if( a >= b || b >= c ) continue;
					if( a*a + b*b == c*c && a+b+c==1000){
						ret= a*b*c;
						num++;
					}
				}
			}
		}
		System.out.println(ret + " " + num);
	}
}


