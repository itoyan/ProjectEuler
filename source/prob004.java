public class prob004 {
	private static int palindromicNumber(){
		String[][] mat = new String[900][900];
		int max = -1;
		for( int i=0 ; i<mat.length ; i++){
			for( int j=0 ; j<mat[i].length ; j++ ){
				mat[i][j] = "" + ((i+100)*(j+100));
				String rev = new StringBuilder(mat[i][j]).reverse().toString();
				if( rev.equals(mat[i][j]) ){
					max = Math.max(max, Integer.parseInt(mat[i][j]));
				}
			}
		}
		return max;
	}
	public static void main(String[] args){
		System.out.println(palindromicNumber());
	}
}
