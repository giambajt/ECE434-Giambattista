#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	uint32_t gpio1 = P9_31;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
while(1){
//	for(i=0; i<10; i++) {
		__R30 |= gpio1;	// The the USR3 LED on

//		__delay_cycles(500000000/5);    	// Wait 1/2 second

		__R30 &= ~gpio1;

//		__delay_cycles(500000000/5); 

	}
//	__halt();
}

// Turns off triggers
#pragma DATA_SECTION(init_pins, ".init_pins")
#pragma RETAIN(init_pins)
const char init_pins[] =  
	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
	"\0\0";
