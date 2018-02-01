# [PackageDev] target_format: plist, ext: tmLanguage
name: Chipsea
scopeName: source.chipsea.assembly
fileTypes: [inc, asm, INC, ASM]
uuid: 6157814c-5c11-4dcf-8d6f-c550b8a8d11a
# ADD HISTORY
# 2017-01-01 Add CSU14PD87
# 2017-01-19 Add CSU18M8X
patterns:
- include: '#registers'

- include: '#mnemonics'

- include: '#constants'

- include: '#comments'

- include: '#entitys'

- include: '#string'

- include: '#keywords'

- include: '#support'

- include: '#function'

- include: '#variables'

- include: '#methods'

- include: '#boolean'

- include: '#storage'

repository:
  comments:
    patterns:
    - name: comment.line.string
      match: (//|;|(^|\s)#\s).*$
    - name: comment.block.string
      begin: /\*
      end: \*/
  constants:
    patterns:
    - name: constant.numeric.floating-point
      match: (?i)\b(([0-9]+\.[0-9]*)(e[+-]?[0-9]+)?|\.?[0-9]+e[+-]?[0-9]+)\b
    - name: constant.numeric.literal
      match: (?i)(\$[0-9a-f]+)\b
    - name: constant.numeric.bin
      match: (?i)\b[01]+b\b
    - name: constant.numeric.oct
      match: (?i)\b[0-7]+[oq]\b
    - name: constant.numeric.dec
      match: (?i)\b[0-9]+\b
    - name: constant.numeric.hex
      match: (?i)\b([0-9a-fA-F]+[hH]|0x[0-9a-fA-F]+)\b

  keywords:
    patterns:
    - comment: Keyword.other.chipsea
      name: keyword.control.chipsea.Instruction
      match: (?i)\b(addlw|addpcw|addwf|addwfc|andlw|andwf|bcf|bsf|btfsc|btfss|call|clrf|clrwdt|comf|daw)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(decf|decfsz|goto|halt|incf|incfsz|iorlw|iorwf|movfw|movlw|movp|movwf|nop|pop|push)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(retfie|retlw|return|rlf|rrf|sleep|sublw|subwf|subwfc|swapf|tblp|xorlw|xorwf)\b
    - comment: mac
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(movlf|movff|movff2|movff3|movff4|movff5|movff6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(sublf|subff|subff2|subff3|subff4|subff5|subff6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(addlf|addff|addff2|addff3|addff4|addff5|addff6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(clrf2|clrf3|clrf4|clrf5|clrf6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(rlf2|rlf3|rlf4|rlf5|rlf6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(rrf2|rrf3|rrf4|rrf5|rrf6)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(addfff3|subfff3)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(jz|jnz|jc|jnc|jb|jnb|je|jne)\b
    # 逻辑运算指令@2018/1/31 15:35:00
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(and|and_into|iand|iand_into|ior|ixor|or|or_into|)\b
    # 运算指令
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(add|sub|div|iadd|isub|idiv|increase|imul32|random|pincrease|mul32)\b
    # 位运算指令
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(lshift|lshift2|lshift3|lshift4|rshift|rshift2|rshift3|rshift4|setflag|nsetflag)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(isolate1|isolate0|qisolate1|qisolate0|set0|set1|byteswap|setflip|qset0|qset1|compare|icompare|invert|reverse)\b
    # 寻址指令
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(jam|hjam|fetch|fetcht|ifetch|ifetcht|hfetch|hfetcht|store|storet|istore|istoret)\b
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(hstore|force|iforce|arg|setarg|copy|deposit|disable|enable)\b
    # 跳转指令
    - name: keyword.control.chipsea.Instruction
      match: (?i)\b(call|rtn|nrtn|rtneq|rtnbit1|rtnbit0|branch|bbit1|bbit0|beq|bne|loop|bpatch|parse)\b

  entitys:
    patterns:
    - name: string.interpolated
      begin: (?i)^\s*[\#%]\s*if\s+0\b
      end:   (?i)^\s*[\#%]\s*endif\b
    - name: string.interpolated
      match: (?i)\b(dw|org|include|end|equ)\b
    - name: string.interpolated
      match: (?i)\b(macro|endm|if|endif)\b
    - name: string.interpolated
      match: (?i)\b(define|high|low|$)\b
    - name: string.interpolated
      match: (?i)\b(bank0|bank1|bank2|bank3|bank4|bank5|bank6|bank7)\b
    - name: string.interpolated
      match: (?i)\b(bankisel|banksel|text|db|#define|ds|dw|dt|else|elseif|end|endif|endm|ends|endw|while|equ|exitm|error|extem|global|section|if|ifdef|ifndef|#include|macro|org|#undefine|warnning|rom|ram|addr)\b
  support:
    patterns:
    - name: support.class
      match: (?i)\b(IND0|IND1|FSR0|FSR1|STATUS|WORK|INTF|INTE|BSR)\b
    - name: support.class
      match: (?i)\b(EADRH|EADRL|EDAT|EOPEN|WDTCON|WDTIN|TMOUT|TMCON|ADOH|ADOL|ADOLL|ADCON)\b
    - name: support.class
      match: (?i)\b(MCK|PCK|MCK2|NETA|NETB|NETC|NETD|NETE|NETF|SVD|PT1|PT1EN|PT1PU|PT1CON)\b
    - name: support.class
      match: (?i)\b(AIENB|PT2|PT2EN|PT2PU|PT4|PT4EN|PT4PU|PT2MR|PT2CON|PTINT|INTF2|INTE2)\b
    - name: support.class
      match: (?i)\b(TM0CON|TM0IN|TM0CNT|TM1CON|TM1IN|TM1CNT|TM1R)\b
    - name: support.class
      match: (?i)\b(LCD1|LCD2|LCD3|LCD4|LCD5|LCD6|LCD7|LCD8|LCD9|LCD10|LCD11|LCD12|lcd13|LCD14|LCD15|LCD16|LCD17|LCD18|LCD19|LCD20|LCD21|LCD22|LCD23|LCD24|LCD25|LCD26|LCD27|LCD28|LCD29|LCD30|LCD31|LCD32|LCD33|LCD34|LCD35|LCD36|LCD37|LCD38|LCD39|LCD40|LCD41|LCD42|LCD43|LCD44|LCD45|LCD46|LCD47|LCD48|LCD49|LCD50|LCD51|LCD52|LCD53|LCD54|LCD55|LCD56|LCD57|LCD58|LCD59|LCD60|LCD61|LCD62|LCD63|LCD64|LCD65|LCD66|LCD67|LCD68|LCD69|LCD70|LCD71)\b
    - name: support.class
      match: (?i)\b(LED1|LED2|LED3|LED4|LED5|LED6|LED7|LED8|LED9|LED10|LED11|LED12|LED14|LED14)\b
    - name: support.class
      match: (?i)\b(LEDCON1|LEDCON2|CHPCON|AD2OH|AD2OL)\b
    - name: support.class
      match: (?i)\b(LCDCN1|LCDENR|TEMPC|WDT_C|IOSC_C|TEST|SCON1|SCON2|SBUF|AIENB)\b
    - name: support.class
      match: (?i)\b(RTCCON|RTCAER|RTCYEAR|RTCMON|RTCDAY|RTCHOUR|RTCMIN|RTCSEC|RTCDWR|INTEGER|FRACTION)\b
      #add 32bit 2018/1/31 15:38:38
    - name: support.class
      match: (?i)\b(pdata|temp|rega|regb|regab|regc|queue|contr|contw|contru|contwu|loopcnt|mark|null|clk_bt|clk_rt|clke_bt|clke_rt|pc)\b


# 2017/4/16 add CSU18M88 Register
    - name: support.class
      match: (?i)\b(PCLOADL|PCLOADH|ROOT|ADCFG|ANACFG|LVDCON|PT3|PT3EN|PT3PU|PT5|PT5EN|PT5PU|PTCON|PTINT0|PTINT1|TM2CON|TM2IN|TM2CNT|TM2R|TM3CON|TM3IN|TM3CNT|TM3R|LCD15|LCD16|LCD17|LCD18|LCD19|LCD20|LCDCN2|INTF3|INTE3|SPICFG|SPICN|SPICKR|SPIDAT|I2CCON|I2CDAT|WDT_TRI|ICK_TRI|VS_TRIM|UR0_CR1|UR0_BRR|UR0_BRR|UR0_TX_|UR0_RX_|UR0_CR2|UR0_ST|UR1_CR1|UR1_BRR|UR1_BRR|UR1_TX_|UR1_RX_|UR1_CR2|UR1_ST|I2CADR|WDT_TRIM|ICK_TRIM|UR0_BRR0|UR0_BRR1|UR0_TX_REG|UR0_RX_REG|UR1_BRR0|UR1_BRR1|UR1_TX_REG|UR1_RX_REG)\b

    - name: support.function
      match: (?i)\b(Z|C|DC|TO|PD)\b
    - name: support.function
      match: (?i)\b(E0IF|E1IF|ADIF|TMIF|AD2IF|TM0IF|TM1IF)\b
    - name: support.function
      match: (?i)\b(E0IE|E1IE|ADIE|TMIE|GIE|AD2IE|TM0IE|TM1IE)\b
    - name: support.function
      match: (?i)\b(PAGE0|PAGE1|IRP1|IRP0)\b
    - name: support.function
      match: (?i)\b(WDTS0|WDTS1|WDTS2|WDTS3|Wdt_lcd|WDTEN|WDTS_0|WDTS_1|WDTS_2)\b
    - name: support.function
      match: (?i)\b(INS0|INS1|INS2|TMEN|TRST)\b
    - name: support.function
      match: (?i)\b(ADM0|ADM1|ADM2|ADSC|ADM_0|ADM_1|ADM_2)\b
    - name: support.function
      match: (?i)\b(M1_CK|M2_CK)\b
    - name: support.function
      match: (?i)\b(S_BEEP0|S_BEEP1|LCDSCKS0|LCDSCKS1|LCDSCKS2|LCDSCKS3)\b
    - name: support.function
      match: (?i)\b(CLK_SEL|M3_CK|EO_SLP|CST_IN|CST_E|XTALSEL|TMSEL0|TMSEL1)\b
    - name: support.function
      match: (?i)\b(CHPCKS0|CHPCKS1|CHPCKS2|CM_SEL|SINL_0|SINL_1|ACM|SINL0|SINL1)\b
    - name: support.function
      match: (?i)\b(ERV)\b
    - name: support.function
      match: (?i)\b(ADEN|ADG0|ADG_0|ADG_1|ADG1|ADG_M0|ADG_M1|CHOPM0|CHOPM1|CHOPM_0|CHOPM_1)\b
    - name: support.function
      match: (?i)\b(LCDREF0|LCDREF1|VLCDX0|VLCDX1|Level_s|LCDCH)\b
    - name: support.function
      match: (?i)\b(ENLB|SILB0|SILB1|SILB2|LDOS0|LDOS1|LB_RST_CON|SILB_0|SILB_1|SILB_2|LDOS_0|LDOS_1)\b
    - name: support.function
      match: (?i)\b(ENVB|BGID0|BGID1|BGID2|BGID3|ENVDDA|LDOEN|LVR_EN|CHP_VPP)\b
    - name: support.function
      match: (?i)\b(LBOUT)\b
    - name: support.function
      match: (?i)\b(AIENB1|AIENB2|AIENB3)\b
    - name: support.function
      match: (?i)\b(E0M0|E0M1|E1M0|E1M1|E0M_0|E0M_1|E1M_0|E1M_1|BZEN)\b
    - name: support.function
      match: (?i)\b(BZSEL|SEGCON0|SEGCON1)\b
    - name: support.function
      match: (?i)\b(PTW0_0|PTW0_1|PTW0_2|PTW1_0|PTW1_1|PTW1_2|PTW1_3)\b
    - name: support.function
      match: (?i)\b(URRIF|URTIF|RTCIF)\b
    - name: support.function
      match: (?i)\b(URRIE|URTIE|RTCIE)\b
    - name: support.function
      match: (?i)\b(T0SEL|T0RSTB|T0RATE_0|T0RATE_1|T0RATE_2|T0EN)\b
    - name: support.function
      match: (?i)\b(PWM1OUT|T1OUT|T1RSTB|T1CKS|T1RATE_0|T1RATE_1|T1RATE_2|T1EN)\b
    - name: support.function
      match: (?i)\b(LED_PMODE|LEDCLKS_0|LEDCLKS_1|LED_DUTY0|LED_DUTY1|LED_DUTY2|LED_Current0|LED_Current1|LED_Current2)\b
    - name: support.function
      match: (?i)\b(LEDEN|CONT_SEL)\b
    - name: support.function
      match: (?i)\b(CSE_LCD)\b
    - name: support.function
      match: (?i)\b(CHPEN|CHPCLKS_0|CHPCLKS_1|CHPCLKS_2|CHPVS)\b
    - name: support.function
      match: (?i)\b(AD2EN)\b
    - name: support.function
      match: (?i)\b(RTCEN|H_24_12|LIR)\b
    - name: support.function
      match: (?i)\b(DWR_0|DWR_1|DWR_2)\b
    - name: support.function
      match: (?i)\b(ENPMPL|LCD_DUTY0|LCD_DUTY1|LEVEL|LCDWS|LCDEN|LCDCKS0|LCDCKS1)\b
    - name: support.function
      match: (?i)\b(WDT_C1|WDT_C2|WDT_C3)\b
    - name: support.function
      match: (?i)\b(UARTENUR0_RNIE||UART_SEL|RB8|TB8|REN|SM2|SM1|SM0)\b
    - name: support.function
      match: (?i)\b(SMOD)\b
    - name: support.function
      match: (?i)\b(W|F)\b
    - name: support.function
      match: (?i)\b(blank|positive|true|user|user2|user3|zero|master|slave|wake|match|timeout|sync|le)\b
# 2017/4/16
    - name: support.variable
      match: (?i)\b(GC_EN|STOP_ERR|RXOV_ERR|TX_BUSY|RX_BUSY|TM2IF|TM2IE|ick_ldo_by|ECK_EN|WDT_CLK_EN|ICK_EN|PROG_BUSY|READ_CHECK|ROOT_EN|I2C_DIV_1|I2C_DIV_0|UART1DIV_2|UART1DIV_1|UART1DIV_0|UART0DIV_2|UART0DIV_1|UART0DIV_0|S_BEEP_1|S_BEEP_0|F_GAIN_1|F_GAIN_0|S_GAIN_1|S_GAIN_0|R_GAIN|BGR_ENB|BGID|AD2START|AD3_SL_3|AD3_SL_2|AD3_SL_1|AD3_SL_0|AD2O_9|AD2O_8|LVDEN|AD2_REF|SMT5_EN|SMT2_EN|SMT1_EN|PT15_VDD|PT14_VDD|I2C_VDD|PWM3_SEL|PWM2_SEL|PWM1_SEL|UR1_RHIF|UR1_RNIF|UR1_THIF|UR1_TEIF|UR0_RHIF|UR0_RNIF|UR0_THIF|UR0_TEIF|UR1_RHIE|UR1_RNIE|UR1_THIE|UR1_TEIE|UR0_RHIE|UR0_RNIE|UR0_THIE|UR0_TEIE|T0SEL_1|T0SEL_0|T2EN|T2RATE_2|T2RATE_1|T2RATE_0|T2CKS|T2RSTB|T2OUT|PWM2OUT|T3EN|T3RATE_2|T3RATE_1|T3RATE_0|T3SEL|T3RSTB|T3OUT|PWM3OUT|LCDFC_1|LCDFC_0|VLCDX_1|VLCDX_0|LCDSCKS_3|LCDSCKS_2|LCDSCKS_1|LCDSCKS_0|LCDFR|LCDREF_2|LCDREF_1|LCDREF_0|LCDCKS_1|LCDCKS_0|LCD_DUTY_1|LCD_DUTY_0|I2C_TIF|I2C_RIF|UR0ERR_IF|UR1WK_IF|UR0WK_IF|TM3IF|SPIIF|I2C_TIE|I2C_RIE|UR0ERR_IE|UR1WK_IE|UR0WK_IE|TM3IE|SPIIE|SPIEN|MSTEN|CKPHA|CKPOL|MULMST|WIREMOD|SPIBSY|SPIRST|SLVSEL|WCOL|MODCOL|RFU|HR_24_12|INTEGER_3|INTEGER_2|INTEGER_1|INTEGER_0|TEN_YEAR_3|TEN_YEAR_2|TEN_YEAR_1|TEN_YEAR_0|ONE_YEAR_3|ONE_YEAR_2|ONE_YEAR_1|ONE_YEAR_0|TEN_MON|ONE_MON_3|ONE_MON_2|ONE_MON_1|ONE_MON_0|TEN_DAY_1|TEN_DAY_0|ONE_DAY_3|ONE_DAY_2|ONE_DAY_1|ONE_DAY_0|AM_PM|TEN_HOUR_1|TEN_HOUR_0|ONE_HOUR_3|ONE_HOUR_2|ONE_HOUR_1|ONE_HOUR_0|TEN_MIN_2|TEN_MIN_1|TEN_MIN_0|ONE_MIN_3|ONE_MIN_2|ONE_MIN_1|ONE_MIN_0|TEN_SEC_2|TEN_SEC_1|TEN_SEC_0|ONE_SEC_3|ONE_SEC_2|ONE_SEC_1|ONE_SEC_0|I2C_EN|AWK_EN|CST_EN|ACK_EN|I2CSTUS_3|I2CSTUS_2|I2CSTUS_1|I2CSTUS_0|TMOD_1|TMOD_0|ICK_SEL_1|ICK_SEL_0|WDT_TRIM_3|WDT_TRIM_2|WDT_TRIM_1|WDT_TRIM_0|sim_rst|LVD_TRIM_2|LVD_TRIM_1|LVD_TRIM_0|VS_TRIM_3|VS_TRIM_2|VS_TRIM_1|VS_TRIM_0|TX9D|RX9D|TX9_EN|RX9_EN|RX_EN|TX_EN|UART_EN)\b
    - name: support.variable
      match: (?i)\b(|RXF_WATER_LEVEL_2|RXF_WATER_LEVEL_1|RXF_WATER_LEVEL_0|TXF_WATER_LEVEL_2|TXF_WATER_LEVEL_1|TXF_WATER_LEVEL_0)\b


  variables:
    patterns:
    - name: support.function
      match: '^\s*(%%)?(\w|[\._?])(\w|[_$#@~\.?])*\:'
    - name: support.function
      match: '^\s*([$@~])(\w|[_$#@~\.?])*\:'
    - name: variable.language
      match: (?i)\b([C]_[(\w|[_$#@~\.?])]*)\b
    - name: support.function
      match: (?i)\b([FL]_[(\w|[_$#@~\.?])]*)\b
    - name: method.chipsea
      match: (?i)\b([R]_[(\w|[_$#@~\.?])]*)\b
    - name: storage.type
      match: (?i)\b([M]_[(\w|[_$#@~\.?])]*)\b
    - name: constant.chipsea
      match: (?i)\b([B]_[(\w|[_$#@~\.?])]*)\b