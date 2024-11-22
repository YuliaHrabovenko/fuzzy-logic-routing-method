import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as cntrl
from skfuzzy.control import Rule as rule

class FIS:
    def __init__(self, energy, speed, hops):
        self.energy = energy
        self.speed = speed
        self.hops = hops
        self.stability = 0

    def fuzzy_controler(self):
        energy = cntrl.Antecedent(np.arange(0, 101, 1), 'Energy')
        speed = cntrl.Antecedent(np.arange(0, 13, 1), 'Speed')
        hops = cntrl.Antecedent(np.arange(0, 11, 1), 'Hops')
        stability = cntrl.Consequent(np.arange(0, 101, 1), 'Stability')

        energy_names = ['low', 'middle', 'high']
        energy.automf(names=energy_names)
        speed_names = ['low', 'middle', 'high']
        speed.automf(names=speed_names)
        hops_names = ['short', 'average', 'long']
        hops.automf(names=hops_names)

        stability_names = ['very_low', 'low', 'medium', 'high', 'very_high']
        stability.automf(names=stability_names)

        stability['very_low'] = fuzz.trapmf(stability.universe, [0, 0, 17, 34])
        stability['low'] = fuzz.trimf(stability.universe, [17, 34, 50])
        stability['medium'] = fuzz.trimf(stability.universe, [34, 50, 68])
        stability['high'] = fuzz.trimf(stability.universe, [50, 68, 84])
        stability['very_high'] = fuzz.trapmf(stability.universe, [68, 84, 100, 100])

        r1 = rule(energy['high'] & speed['high'] & hops['long'], stability['very_low'])
        r2 = rule(energy['high'] & speed['high'] & hops['average'], stability['very_low'])
        r3 = rule(energy['high'] & speed['high'] & hops['short'], stability['low'])
        r4 = rule(energy['high'] & speed['middle'] & hops['long'], stability['low'])
        r5 = rule(energy['high'] & speed['middle'] & hops['average'], stability['medium'])
        r6 = rule(energy['high'] & speed['middle'] & hops['short'], stability['very_high'])
        r7 = rule(energy['high'] & speed['low'] & hops['long'], stability['medium'])
        r8 = rule(energy['high'] & speed['low'] & hops['average'], stability['high'])
        r9 = rule(energy['high'] & speed['low'] & hops['short'], stability['very_high'])
        r10 = rule(energy['middle'] & speed['high'] & hops['long'], stability['very_low'])
        r11 = rule(energy['middle'] & speed['high'] & hops['average'], stability['low'])
        r12 = rule(energy['middle'] & speed['high'] & hops['short'], stability['low'])
        r13 = rule(energy['middle'] & speed['middle'] & hops['long'], stability['low'])
        r14 = rule(energy['middle'] & speed['middle'] & hops['average'], stability['medium'])
        r15 = rule(energy['middle'] & speed['middle'] & hops['short'], stability['high'])
        r16 = rule(energy['middle'] & speed['low'] & hops['long'], stability['medium'])
        r17 = rule(energy['middle'] & speed['low'] & hops['average'], stability['high'])
        r18 = rule(energy['middle'] & speed['low'] & hops['short'], stability['high'])
        r19 = rule(energy['low'] & speed['high'] & hops['long'], stability['very_low'])
        r20 = rule(energy['low'] & speed['high'] & hops['average'], stability['very_low'])
        r21 = rule(energy['low'] & speed['high'] & hops['short'], stability['low'])
        r22 = rule(energy['low'] & speed['middle'] & hops['long'], stability['very_low'])
        r23 = rule(energy['low'] & speed['middle'] & hops['average'], stability['very_low'])
        r24 = rule(energy['low'] & speed['middle'] & hops['short'], stability['low'])
        r25 = rule(energy['low'] & speed['low'] & hops['long'], stability['very_low'])
        r26 = rule(energy['low'] & speed['low'] & hops['average'], stability['low'])
        r27 = rule(energy['low'] & speed['low'] & hops['short'], stability['low'])

        stability.view()
        energy.view()
        speed.view()
        hops.view()

        stability_ctrl = cntrl.ControlSystem(
            [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15,
             r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27])

        stability_show = cntrl.ControlSystemSimulation(stability_ctrl)
        stability_show.input['Energy'] = self.energy
        stability_show.input['Speed'] = self.speed
        stability_show.input['Hops'] = self.hops

        # Crisp numbers
        stability_show.compute()

        stability.view(sim=stability_show)
        energy.view(sim=stability_show)
        speed.view(sim=stability_show)
        hops.view(sim=stability_show)
        self.stability = stability_show.output['Stability']
