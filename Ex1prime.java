import java.io.*;
class Ex1prime{
  public static void main(String[] args) throws Exception{
    int n;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    System.out.print("Enter a number: ");
    n = Integer.parseInt(br.readLine());
    if(n<2){
      System.out.println(n+" Not a prime number");
    } else{
      for (int i=2;i<n/2;i++){
        if(n%i==0){
          System.out.println(n+" Not a prime number");
          return;
        }
      }
      System.out.println(n+" is a prime number");
    }
      
    }
}

