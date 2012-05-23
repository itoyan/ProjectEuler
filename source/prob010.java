public class prob010{
	public static void main(String[] args){
		int num = Integer.parseInt(args[0]);
		long ret = 0;
		for( int i=2 ; i<=num ; i++ ){
			if( isPrime(i) ) ret += i;
		}
		System.out.println(ret);
	}
	static boolean isPrime(int num){
		int to = (int)Math.sqrt(num);
		for( int i=2 ; i<=to ; i++ ){
			if( num%i == 0 ) return false;
		}
		return true;
	}
}