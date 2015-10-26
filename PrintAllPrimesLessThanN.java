
public class PrintAllPrimesLessThanN {
	public static void main(String[] args){
		int N = 50;
		printAllPrimesLessThanN(N);
	}
	static void printAllPrimesLessThanN(int N){
		
		// initialize boolean array where all values are prime
		boolean[] isPrime = new boolean[N+1];
		for(int i = 2; i < N; i++){
			isPrime[i] = true;
		}
		
		// make non-primes false using Sieve of Eratosthenes
		for(int i = 2; i <= Math.sqrt(N); i++){
			if(isPrime[i]){
				for(int k = i; i * k <= N; k++){
					isPrime[i*k] = false;
				}
			}
		}
		
		// print all primes less than N
		for(int i = 2; i < N; i++){
			if(isPrime[i]){
				System.out.printf("%d ", i);
			}
		}
	}
}
