#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#define PWM_PIN 18
#define PWM_FRQ 50
#define SLEEP_TIME_IN_SECONDS 3
#define DUTY_CYCLE_PERCENTAGE_CENTER 9
#define DUTY_CYCLE_PERCENTAGE_MIN 5
#define DUTY_CYCLE_PERCENTAGE_MAX 12

int dc_int(int dc_perc);

/* 
    PWM control for servo motor, duty cycle 
    between 0.05 (5%) and 0.1 (10%), 0.075 (7.5%) is mid 

    0% dc   --> 0 int
    5% dc   --> 13 int --> -90°
    7.5% dc --> 19 int --> 0°
    9 % dc  --> 23 int
    10% dc  --> 26 int --> +90°
    100% dc --> 255 int
*/
int main()
{
    if (gpioInitialise() < 0) {
        printf("Failed to initialize\n");
        return -1;
    }

    int dc = dc_int(DUTY_CYCLE_PERCENTAGE_CENTER);
    int dc_center = dc_int(DUTY_CYCLE_PERCENTAGE_CENTER);
    int dc_max = dc_int(DUTY_CYCLE_PERCENTAGE_MAX);
    int dc_min = dc_int(DUTY_CYCLE_PERCENTAGE_MIN);
    char char_read;

    gpioSetPWMfrequency(PWM_PIN, PWM_FRQ);
    gpioPWM(PWM_PIN, dc);

    printf(
        "Press a to go left\n"
        "Press s to center\n"
        "Press d to go right\n"
        "Press p to exit\n"
    );

    /* Do stuff */
    for (;;) {
        char_read = getchar();

        if (char_read == 'p')
            break;

        switch (char_read) {
        case 'a':
            /* go right */
            if (dc < dc_max) {
                dc += 1;
                gpioPWM(PWM_PIN, dc);
            }
            break;
        case 'd':
            /* go left */
            if (dc > dc_min) {
                dc -= 1;
                gpioPWM(PWM_PIN, dc);
            }
            break;
        case 's':
            /* center servo */
            dc = dc_center;
            gpioPWM(PWM_PIN, dc);
            break;
        
        default:
            break;
        }
    }

    gpioPWM(PWM_PIN, 0);    
    gpioTerminate();
    
    return 0;
}

int dc_int(int dc_perc)
{
    return (dc_perc / 100.0) * 255;
}
