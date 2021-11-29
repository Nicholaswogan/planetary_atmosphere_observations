import numpy as np

def retrieve_species(sp, data):
    out = []
    for i in range(len(data[sp])):
        entry = {}
        entry['citation'] = data[sp][i]['citation']
        keys = set([key for key in data[sp][i]['data'][0].keys()])
        P_keys = set(['P', 'P-low', 'P-high'])
        alt_keys = set(['alt', 'alt-low', 'alt-high'])

        if bool(keys & P_keys):
            # We have P vs mix
            entry['P'] = []
            entry['P-err'] = []
            for j in range(len(data[sp][i]['data'])):

                P_low_p = True
                if 'P-low' in data[sp][i]['data'][j]:
                    P_low = data[sp][i]['data'][j]['P-low']
                else:
                    P_low_p = False 
                P_high_p = True
                if 'P-high' in data[sp][i]['data'][j]:
                    P_high = data[sp][i]['data'][j]['P-high']
                else:
                    P_high_p = False
                P_p = True
                if 'P' in data[sp][i]['data'][j]:
                    P = data[sp][i]['data'][j]['P']
                else:
                    P_p = False

                if P_p and P_low_p and P_high_p:
                    entry['P'].append(P)
                    tmp = [P - P_low, P_high - P]
                    entry['P-err'].append(tmp)
                elif not P_p and P_low_p and P_high_p:
                    P_tmp = np.mean([P_low,P_high])
                    entry['P'].append(P_tmp)
                    tmp = [P_tmp - P_low, P_high - P_tmp]
                    entry['P-err'].append(tmp)
                elif P_p and not P_low_p and not P_high_p:
                    entry['P'].append(P)
                    tmp = [0,0]
                    entry['P-err'].append(tmp)
                else:
                    raise Exception("Problem parsing data file")

            entry['P'] = np.array(entry['P'])
            entry['P-err'] = np.array(entry['P-err']).T
        elif bool(keys & alt_keys):
            # We have alt vs mix
            entry['alt'] = []
            entry['alt-err'] = []
            for j in range(len(data[sp][i]['data'])):

                alt_low_p = True
                if 'alt-low' in data[sp][i]['data'][j]:
                    alt_low = data[sp][i]['data'][j]['alt-low']
                else:
                    alt_low_p = False 
                alt_high_p = True
                if 'alt-high' in data[sp][i]['data'][j]:
                    alt_high = data[sp][i]['data'][j]['alt-high']
                else:
                    alt_high_p = False
                alt_p = True
                if 'alt' in data[sp][i]['data'][j]:
                    alt = data[sp][i]['data'][j]['alt']
                else:
                    alt_p = False

                if alt_p and alt_low_p and alt_high_p:
                    entry['alt'].append(alt)
                    tmp = [alt - alt_low, alt_high - alt]
                    entry['alt-err'].append(tmp)
                elif not alt_p and alt_low_p and alt_high_p:
                    alt_tmp = np.mean([alt_low,alt_high])
                    entry['alt'].append(alt_tmp)
                    tmp = [alt_tmp - alt_low, alt_high - alt_tmp]
                    entry['alt-err'].append(tmp)
                elif alt_p and not alt_low_p and not alt_high_p:
                    entry['alt'].append(alt)
                    tmp = [0,0]
                    entry['alt-err'].append(tmp)
                else:
                    raise Exception("Problem parsing data file")

            entry['alt'] = np.array(entry['alt'])
            entry['alt-err'] = np.array(entry['alt-err']).T
        else:
            raise Exception("Problem parsing data file")

        # We have P vs mix
        entry['mix'] = []
        entry['mix-err'] = []
        for j in range(len(data[sp][i]['data'])):

            mix_low_p = True
            if 'mix-low' in data[sp][i]['data'][j]:
                mix_low = data[sp][i]['data'][j]['mix-low']
            else:
                mix_low_p = False 
            mix_high_p = True
            if 'mix-high' in data[sp][i]['data'][j]:
                mix_high = data[sp][i]['data'][j]['mix-high']
            else:
                mix_high_p = False
            mix_p = True
            if 'mix' in data[sp][i]['data'][j]:
                mix = data[sp][i]['data'][j]['mix']
            else:
                mix_p = False

            if mix_p and mix_low_p and mix_high_p:
                entry['mix'].append(mix)
                tmp = [mix - mix_low, mix_high - mix]
                entry['mix-err'].append(tmp)
            elif not mix_p and mix_low_p and mix_high_p:
                mix_tmp = np.mean([mix_low,mix_high])
                entry['mix'].append(mix_tmp)
                tmp = [mix_tmp - mix_low, mix_high - mix_tmp]
                entry['mix-err'].append(tmp)
            elif mix_p and not mix_low_p and not mix_high_p:
                entry['mix'].append(mix)
                tmp = [0,0]
                entry['mix-err'].append(tmp)
            else:
                raise Exception("Problem parsing data file")

        entry['mix'] = np.array(entry['mix'])
        entry['mix-err'] = np.array(entry['mix-err']).T

        out.append(entry)
    return out