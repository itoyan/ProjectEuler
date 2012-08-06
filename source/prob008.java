public class prob008{
	final static String num =
		"7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494" +
		"95459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871" +
		"11217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724" +
		"2712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395" +
		"8644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004" +
		"7482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652" +
		"9476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724" +
		"4284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561" +
		"882670428252483600823257530420752963450";
	private static int fiveConsectiveProduct(){
		int max = -1;
		for( int i=0 ; i<num.length()-5 ; i++ ){
			int tmp = 1;
			for( int j=0 ; j<5 ; j++ ){
				tmp *= num.charAt(i+j)-'0';
			}
			max = Math.max(max, tmp);
		}
		return max;
	}
	public static void main(String[] args){
		System.out.println(fiveConsectiveProduct());
	}
}