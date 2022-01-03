import TouchHistoryMath from "react-native/Libraries/Interaction/TouchHistoryMath";

export class HashTable {
    constructor(length) {
        this.length = length;
        this.Table = new Array(length).fill(null);
    }


    myhasher(key){
        var dummy = 0;
        for (const letter of key) {
            dummy = (dummy + (letter.charCodeAt(0) * 47)) % this.length;
        }
        return dummy;
    }



    print_table(){
        this.Table.forEach(function(item, index) {
            console.log(index, item)
          })
    }


    set_item(key, value){
        var index = this.myhasher(key);
        if (this.Table[index] == null) {
            this.Table[index] = []
        }
        this.Table[index].push([key,value])
    }


    get_item(key){
        index = this.myhasher(key)
        if (this.Table[index] == null) {
            return false
        } else {
            for (var i= 0; i < this.length; i++) {
                if (this.Table[index][i][0] == key) {
                    return this.Table[index][i][1]
                }
            }
        }
    }


}

//     def get_item(self,key):
//         index = self.myhasher(key)
//         if self.Table[index] is None:
//             return False
//         else:
//             for i in range(len(self.Table[index])):
//                 if self.Table[index][i][0] == key:
//                     return self.Table[index][i][1]