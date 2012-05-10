public class prob012{
	public static void main(String[] args){
		int i = 1;
		int n = 0;
		while( true ){
			n += i;
			int nDivisors = 0;
			for( int j=1 ; j<=n/2 ; j++ ){
				if( n % j == 0 ) nDivisors++;
			}
			nDivisors++;
			if( nDivisors > 500 ) break;
			i++;
			if( i % 100 == 0 ) System.out.println(i + " " + nDivisors );
		}
		System.out.println(n + " " + i); // 76576500 12375
	}
}
	
