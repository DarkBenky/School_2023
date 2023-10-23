using System;

class Program {
    static void Main(string[] args) {
        
        public class Rectangle {
            public double Width
            public double Height
            public int Area() {
                return Width * Height;
            }
        }

        public class square : Rectangle {
            public double Side
            public new int Area() {
                return Side * Side;
            }
        }

        public abstract class Animal {
            public string Name
            public abstract void Move();
        }

        public class Lion : Animal {
            public override void Move() {
                Console.WriteLine("Lion is moving");
            }
        }

        public class Elephant : Animal {
            public override void Move() {
                Console.WriteLine("Elephant is moving");
            }
        }

        public class Eagle : Animal {
            public override void Move() {
                Console.WriteLine("Eagle is moving");
            }
        }

    }
}
