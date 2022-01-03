async function UDNexe(binary) {
  if (UDNexe.debug) console.group(`[%cudnexe%c] program %c#${++UDNexe.runCount}%c run.`,'color: lime','color: unset','color: cyan','color: unset');
  for (let pointer = 0; pointer < binary.length; pointer++) {
    function getTheNextBytes(count) {
      if (UDNexe.debug) console.log(`[%cudnexe%c] getting %c${count}%c bytes from the current pointer position(%c${pointer}%c).`,'color: lime;','color: unset;','color: cyan;','color: unset;','color: cyan','color: unset')
      var ducks = [];
      for (let i = 0; i < count; i++) {
        var value = binary[++pointer];
        if (value === 0xf3 && binary[pointer+2] === 0) {
          // it's a variable!
          value = UDNexe.memory[binary[pointer+1]];
          pointer += 2;
        }
        ducks.push(value);
      }
      if (UDNexe.debug) console.log(`[%cudnexe%c] now moving the pointer to position %c${pointer}`,'color: lime','color: unset', 'color: cyan;')
      return ducks;
    }
    function writeStringToMemory(string, start) {
      if (UDNexe.debug) console.log(`[%cudnexe%c] writing string %c"${string}"%c to memory address %c0x${start.toString(16)}`,'color: lime','color: unset','color: red;','color: unset','color: cyan');
      var strBytes = string.split('').map(x => x.charCodeAt(0));
      for (let i = 0; i < strBytes.length; i++) {
        UDNexe.memory[start+i] = strBytes[i];
      }
    }
    function getStringFromMemory(startAddress) {
      console.log(`[%cudnexe%c] getting string from the memory address %c0x${startAddress.toString(16)}`,'color: lime;','color: unset;', 'color: cyan;')
      var strBytes = [];
      while (UDNexe.memory[startAddress++] !== 0) {strBytes.push(UDNexe.memory[startAddress-1])};
      var strArr = strBytes.map(x => String.fromCharCode(x));
      var str = strArr.join('');
      return str;
    }
		function findPositionFromLineIndex(index) {
			let newlines = 0;
			let prevIndex = 0;
			if (index === 0) return 0;
			for (let i = 0; i < binary.length; i++) {
				let byte = binary[i];
				if (byte === 0x0a) {
					if (newlines++ === index) {
						return prevIndex;
					} else {
						prevIndex = i;
					}
				}
			}
			return -1;
		}
    let instruction = binary[pointer];
    /*switch (instruction) {
      case 0x08: // writes a number value to memory
        var [memoryAddress, value] = getTheNextBytes(2);
        UDNasm.memory[memoryAddress] = value;
        break;
      case 0x09: // writes a string value to memory
        var [memoryAddress] = getTheNextBytes(1);
        var str = ""
        while (binary[++pointer] !== 0) {str += String.fromCharCode(binary[pointer])};
        str += "\0"
        writeStringToMemory(str, memoryAddress);

        break;
      case 0x0A: // outputs a number value from memory
        var [memoryAddress] = getTheNextBytes(1);
        UDNasm.stdout(UDNasm.memory[memoryAddress]);
        break;
      case 0x0B: // outputs a unicode character value from memory
        var [memoryAddress] = getTheNextBytes(1);
        UDNasm.stdout(String.fromCharCode(UDNasm.memory[memoryAddress]));
        break;
      case 0x0C: // outputs a string value from memory
        var [startAddress] = getTheNextBytes(1);
        var str = getStringFromMemory(startAddress);
        UDNasm.stdout(str);
        break;
      case 0x0D:
        var [startAddress, endAddress, value] = getTheNextBytes(3);
        for (let i = startAddress; i < endAddress; i++) {
          UDNasm.memory[i] = value;
        }
        break;
      
      default:
        UDNasm.error('Unknown instruction: '+instruction);
        break;
    }*/
    let gotod = -1;
    let _break = false;
    if (!UDNexe.instructions[instruction]) return UDNexe.error('Unknown instruction: '+instruction);
    if (UDNexe.debug) console.group(`[%cudnexe%c] instruction %c${instruction}%c (hex %c0x${instruction.toString(16)}%c); pointer: %c${pointer}`,'color: lime;','color: unset;','color: cyan;','color: unset;','color: cyan;','color: unset;','color: cyan;')
    let result = UDNexe.instructions[instruction]({
      getTheNextBytes, writeStringToMemory, getStringFromMemory,
      binary,
      movePointer(x) {
        if (UDNexe.debug) console.log(`[%cudnexe%c] moving pointer to %c${x}`,'color: lime','color: unset','color: cyan');
        pointer = x
      },
      goto(x) {
        if (UDNexe.debug) console.log(`[%cudnexe%c] %cgoto%c :%c${x}`,'color: lime','color: unset','color: blue','color: unset','color: cyan')
        gotod = x;
      },
      getPointer() {return pointer},
      setBreak(x) {_break = x}
    });
    if (result instanceof Promise) {
      await result;
    }
    if (gotod > -1) {
			let pos = findPositionFromLineIndex(gotod);
			if (pos < 0) return UDNexe.error('Invalid line index');
			pointer = pos-1;
			
		}
    if (UDNexe.debug) console.groupEnd();
    if (_break) break;
  }
  /*if(UDNexe.compareFlag=true){
    if(UDNexe.skipducked==false){
      UDNexe.skipducked = true;
    }
    else{
      UDNexe.skipducked = false;
      UDNexe.compareFlag = false;
    }
  }*/

  if (UDNexe.debug) {
    for (let i = 0; i < 20; i++) {
      console.groupEnd(); //y'know just to make sure the group has ended
    } 
  }
}
let sleep = ms => new Promise(r => setTimeout(r,ms));
UDNexe.debug = true;
UDNexe.runCount = 0;
UDNexe.instructions = {
  0x0() {},
	0x0a() {},
  0x08({getTheNextBytes}) {
    var [memoryAddress, value] = getTheNextBytes(2);
    if (memoryAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    if (memoryAddress < 0) return UDNexe.error('Segmentation fault');
    console.log(`[%cudnasm%c] writing %c${value}%c to memory address %c$%c${memoryAddress}`,'color: lime','color: unset','color: cyan','color: unset','color: red','color: blue');
    UDNexe.memory[memoryAddress] = value;
  },
  0x09({getTheNextBytes, writeStringToMemory, binary, pointer, movePointer, getPointer}) {
    var [memoryAddress] = getTheNextBytes(1);
    if (memoryAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    
    var str = ""
    var rpointer = getPointer()
    while (binary[++rpointer] !== 0) {str += String.fromCharCode(binary[rpointer])};
    movePointer(rpointer);
    str += "\0"
    writeStringToMemory(str, memoryAddress);
  },
  0x1A({getTheNextBytes}) {
    var [memoryAddress] = getTheNextBytes(1);
    if (memoryAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    if (memoryAddress < 0) return UDNexe.error('Segmentation fault');
    
    UDNexe.stdout(UDNexe.memory[memoryAddress]);
    console.log(`[%cudnexe%c] [pseudocode] %cprint%c(memory[0x${memoryAddress.toString(16)}] %c${UDNexe.memory[memoryAddress]}%c);`,'color: lime','color: unset','color: blue','color: unset','font-style: italic; color: gray;','font-style: unset; color: unset;');
  },
  0x0B({getTheNextBytes}) {
    var [memoryAddress] = getTheNextBytes(1);
    if (memoryAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    if (memoryAddress < 0) return UDNexe.error('Segmentation fault');
    
    UDNexe.stdout(String.fromCharCode(UDNexe.memory[memoryAddress]));
  },
  0x0C({getTheNextBytes, getStringFromMemory}) {
    var [startAddress] = getTheNextBytes(1);
    if (startAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    if (startAddress < 0) return UDNexe.error('Segmentation fault');
    
    var str = getStringFromMemory(startAddress);
    UDNexe.stdout(str);
    console.log(`[%cudnexe%c] [pseudocode] %cprint%c(%c"${str}"%c);`,'color: lime','color: unset','color: blue','color: unset','color: red','color: unset;');
  },
  0x0D({getTheNextBytes}) {
    var [startAddress, endAddress, value] = getTheNextBytes(3);
    if (startAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    if (startAddress < 0) return UDNexe.error('Segmentation fault');
    console.log(`[%cudnasm%c] fill memory with %c${value}%c starting from the address range of: %c$%c${startAddress}%c-%c$%c${endAddress}`,'color: lime','color: unset', 'color: cyan','color: unset','color: red','color: blue','color: unset','color: red','color: blue')
    for (let i = startAddress; i < endAddress; i++) {
      UDNexe.memory[i] = value;
    }
  },
  0x0E({getTheNextBytes}) {
    var [memAddress, operationId, x, y] = getTheNextBytes(4);
    if (memAddress > UDNexe.memory.length) return UDNexe.error('Segmentation fault');
    var operations = ['+','-','*','/'];
    var operation = operations[operationId];
    console.log(`[%cudnexe%c] running math operation: %c${x} %c${operation} %c${y}`,'color: lime','color: unset','color: cyan','color: blue','color: cyan');
    console.log(`[%cudnexe%c] [pseudocode] %c$%c0x${memAddress.toString(16)} %c= %c${x} %c${operation} %c${y}`,'color: lime','color: unset','color: red','color: blue','color: gold','color: blue','color: unset','color: blue');
    switch (operation) {
      case '+':
        UDNexe.memory[memAddress] = x + y;
        break;
      case '-':
        UDNexe.memory[memAddress] = x - y;
        break;
      case '*':
        UDNexe.memory[memAddress] = x * y;
        break;
      case '/':
        UDNexe.memory[memAddress] = x + y;
        break;
      
    }
  },
  0x0F({goto, getTheNextBytes, binary}) {
    var [position] = getTheNextBytes(1);
    if (position < 0) return UDNexe.error('Invalid pointer position');
    if (position > binary.length) return UDNexe.error('Pointer position overflow');
    goto(position);
  },
  0x10({getTheNextBytes}) {
    var [ms] = getTheNextBytes(1);
    if (ms < 0) return UDNexe.error('Invalid sleep delay');
    console.log('[%cudnexe%c] %csleep %c'+ms,'color: lime','color: unset','color: blue','color: cyan')
    return sleep(ms);
  },
  0x11({getTheNextBytes, goto}) { // AND operator don't forget
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    
    console.log(`[%cudnexe%c] AND operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan')
    if (leftAddress && rightAddress) {
      goto(thenPos);
    }
  },
  0x12({getTheNextBytes, goto}) { // OR operator don't forget 
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    console.log(`[%cudnexe%c] OR operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan')
    if (leftAddress || rightAddress) {
      goto(thenPos);
    }
  },
  0x13({getTheNextBytes, goto}) { // EQUAL operator don't forget
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    console.log(`[%cudnexe%c] EQUAL operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan')
    if (leftAddress === rightAddress) {
      goto(thenPos);
    }
  },
  0x14({getTheNextBytes, goto}) { // NOT EQUAL operator don't forget
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    console.log(`[%cudnexe%c] NOT EQUAL operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan')
    if (leftAddress !== rightAddress) {
      goto(thenPos);
    }
  },
  0x15({setBreak}) { // basically return;
    console.log('[%cudnexe%c] %creturn%c;','color: lime','color: unset','color: blue','color: unset');
    setBreak(true);
  },
  0x16({getTheNextBytes, goto}) { // LESS THAN operator don't forget
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    console.log(`[%cudnexe%c] LESS THAN operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan');
    
    if (leftAddress < rightAddress) {
      goto(thenPos);
    }
  },
  0x17({getTheNextBytes, goto}) { // HIGHER THAN operator don't forget
    var [leftAddress, rightAddress, thenPos] = getTheNextBytes(3);
    console.log(`[%cudnexe%c] HIGHER THAN operator %c$%c${leftAddress}%c, %c$%c${rightAddress}%c; jump :%c${thenPos}`,'color: lime','color: unset','color: red','color: blue','color: unset','color: red','color: blue','color: unset','color: cyan')
    if (leftAddress > rightAddress) {
      goto(thenPos);
    }
  },
  
  /*0x11({getTheNextBytes}) {
    var [leftIsAddress, rightIsAddress, leftThing, rightThing] = getTheNextBytes(4);
    if(leftIsAddress==0x01){
      leftThing = UDNexe.memory[leftThing];
    }
    if(rightIsAddress==0x01){
      rightThing = UDNexe.memory[rightThing];
    } 
    UDNexe.compareFlag = leftThing==rightThing;
  },
  0x12({goto, getTheNextBytes}) {
    var [position] = getTheNextBytes(1);
    if(UDNexe.compareFlag){
      goto(position+1);
    }
  },
  0x13({goto, getTheNextBytes}) {
    var [position] = getTheNextBytes(1);
    if(!UDNexe.compareFlag){
      goto(position+1);
    }
  }*/
}
UDNexe.writeStringToMemory = function writeStringToMemory(string, start) {
  if (start < 0) throw 'Segmentation fault';
  if (start > UDNexe.memory.length) throw 'Segmentation fault';
  var strBytes = string.split('').map(x => x.charCodeAt(0));
  for (let i = 0; i < strBytes.length; i++) {
    UDNexe.memory[start+i] = strBytes[i];
  }
  return {start, end: start+strBytes.length};
}
UDNexe.getStringFromMemory = function getStringFromMemory(startAddress) {
  if (startAddress < 0) throw 'Segmentation fault';
  if (startAddress > UDNexe.memory.length) throw 'Segmentation fault';
  var strBytes = [];
  while (UDNexe.memory[startAddress++] !== 0) {strBytes.push(UDNexe.memory[startAddress-1])};
  var strArr = strBytes.map(x => String.fromCharCode(x));
  var str = strArr.join('');
  return str;
}
UDNexe.getMemoryRegion = function getMemoryRegion(start, end) {
  if (start < 0) throw 'Segmentation fault';
  if (start > UDNexe.memory.length) throw 'Segmentation fault';

  if (end < start) throw 'Invalid range';
  if (end < 0) throw 'Invalid range';
  if (end > UDNexe.memory.length) throw 'Segmentation fault';
  var ducks = [];
  for (let i = start; i < end; i++) {
    ducks.push(UDNexe.memory[i]);
  }
  return ducks;
}
UDNexe.writeArrayToMemory = function writeArrayToMemory(arr, start) {
  if ((start+arr.length) > UDNexe.memory.length) throw 'Segmentation fault';
  for (let i = 0; i < arr.length; i++) {
    UDNexe.memory[start+i] = arr[i];
  }
  return {start, end: arr.length+start};
}
UDNexe.stringToBytes = function(str) {
  return str.split('').map(x => x.charCodeAt(0))
}
UDNexe.stdout = function(data) {
  return console.log(data);
}
UDNexe.error = function(data) {
  return console.error(data);
}
UDNexe.memory = new Uint32Array(1024);
UDNexe.runFromMemory = function(start, end) {
  return UDNexe(UDNexe.getMemoryRegion(start, end))
}
