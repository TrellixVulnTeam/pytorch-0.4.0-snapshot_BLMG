# This file is part of PeachPy package and is licensed under the Simplified BSD license.
#    See license.rst for the full text of the license.

import peachpy

import peachpy.arm.abi
import peachpy.arm.isa

from peachpy.arm.microarchitecture import Microarchitecture
from peachpy.arm.registers import GeneralPurposeRegister, SRegister, DRegister, QRegister, WMMXRegister, \
    r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, lr, pc, \
    s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, \
    s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, \
    d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, \
    q0, q1, q2, q3, q4, q5, q6, q7, \
    wr0, wr1, wr2, wr3, wr4, wr5, wr6, wr7, wr8, wr9, wr10, wr11, wr12, wr13, wr14, wr15
from peachpy.arm.function import Function

from peachpy.arm.pseudo import Label, Loop, \
    LABEL, ALIGN, RETURN, LOAD, STORE, ASSUME, INIT, REDUCE, SWAP

from peachpy.arm.generic import \
    ADD, ADDEQ, ADDNE, ADDCS, ADDHS, ADDCC, ADDLO, ADDMI, ADDPL, ADDVS, \
    ADDVC, ADDHI, ADDLS, ADDGE, ADDLT, ADDGT, ADDLE, \
    ADDS, ADDSEQ, ADDSNE, ADDSCS, ADDSHS, ADDSCC, ADDSLO, ADDSMI, ADDSPL, \
    ADDSVS, ADDSVC, ADDSHI, ADDSLS, ADDSGE, ADDSLT, ADDSGT, ADDSLE, \
    ADC, ADCEQ, ADCNE, ADCCS, ADCHS, ADCCC, ADCLO, ADCMI, ADCPL, ADCVS, \
    ADCVC, ADCHI, ADCLS, ADCGE, ADCLT, ADCGT, ADCLE, \
    ADCS, ADCSEQ, ADCSNE, ADCSCS, ADCSHS, ADCSCC, ADCSLO, ADCSMI, ADCSPL, \
    ADCSVS, ADCSVC, ADCSHI, ADCSLS, ADCSGE, ADCSLT, ADCSGT, ADCSLE, \
    SUB, SUBEQ, SUBNE, SUBCS, SUBHS, SUBCC, SUBLO, SUBMI, SUBPL, SUBVS, \
    SUBVC, SUBHI, SUBLS, SUBGE, SUBLT, SUBGT, SUBLE, \
    SUBS, SUBSEQ, SUBSNE, SUBSCS, SUBSHS, SUBSCC, SUBSLO, SUBSMI, SUBSPL, \
    SUBSVS, SUBSVC, SUBSHI, SUBSLS, SUBSGE, SUBSLT, SUBSGT, SUBSLE, \
    SBC, SBCEQ, SBCNE, SBCCS, SBCHS, SBCCC, SBCLO, SBCMI, SBCPL, SBCVS, \
    SBCVC, SBCHI, SBCLS, SBCGE, SBCLT, SBCGT, SBCLE, \
    SBCS, SBCSEQ, SBCSNE, SBCSCS, SBCSHS, SBCSCC, SBCSLO, SBCSMI, SBCSPL, \
    SBCSVS, SBCSVC, SBCSHI, SBCSLS, SBCSGE, SBCSLT, SBCSGT, SBCSLE, \
    RSB, RSBEQ, RSBNE, RSBCS, RSBHS, RSBCC, RSBLO, RSBMI, RSBPL, RSBVS, \
    RSBVC, RSBHI, RSBLS, RSBGE, RSBLT, RSBGT, RSBLE, \
    RSBS, RSBSEQ, RSBSNE, RSBSCS, RSBSHS, RSBSCC, RSBSLO, RSBSMI, RSBSPL, \
    RSBSVS, RSBSVC, RSBSHI, RSBSLS, RSBSGE, RSBSLT, RSBSGT, RSBSLE, \
    RSC, RSCEQ, RSCNE, RSCCS, RSCHS, RSCCC, RSCLO, RSCMI, RSCPL, RSCVS, \
    RSCVC, RSCHI, RSCLS, RSCGE, RSCLT, RSCGT, RSCLE, \
    RSCS, RSCSEQ, RSCSNE, RSCSCS, RSCSHS, RSCSCC, RSCSLO, RSCSMI, RSCSPL, \
    RSCSVS, RSCSVC, RSCSHI, RSCSLS, RSCSGE, RSCSLT, RSCSGT, RSCSLE, \
    AND, ANDEQ, ANDNE, ANDCS, ANDHS, ANDCC, ANDLO, ANDMI, ANDPL, ANDVS, \
    ANDVC, ANDHI, ANDLS, ANDGE, ANDLT, ANDGT, ANDLE, \
    ANDS, ANDSEQ, ANDSNE, ANDSCS, ANDSHS, ANDSCC, ANDSLO, ANDSMI, ANDSPL, \
    ANDSVS, ANDSVC, ANDSHI, ANDSLS, ANDSGE, ANDSLT, ANDSGT, ANDSLE, \
    BIC, BICEQ, BICNE, BICCS, BICHS, BICCC, BICLO, BICMI, BICPL, BICVS, \
    BICVC, BICHI, BICLS, BICGE, BICLT, BICGT, BICLE, \
    BICS, BICSEQ, BICSNE, BICSCS, BICSHS, BICSCC, BICSLO, BICSMI, BICSPL, \
    BICSVS, BICSVC, BICSHI, BICSLS, BICSGE, BICSLT, BICSGT, BICSLE, \
    ORR, ORREQ, ORRNE, ORRCS, ORRHS, ORRCC, ORRLO, ORRMI, ORRPL, ORRVS, \
    ORRVC, ORRHI, ORRLS, ORRGE, ORRLT, ORRGT, ORRLE, \
    ORRS, ORRSEQ, ORRSNE, ORRSCS, ORRSHS, ORRSCC, ORRSLO, ORRSMI, ORRSPL, \
    ORRSVS, ORRSVC, ORRSHI, ORRSLS, ORRSGE, ORRSLT, ORRSGT, ORRSLE, \
    EOR, EOREQ, EORNE, EORCS, EORHS, EORCC, EORLO, EORMI, EORPL, EORVS, \
    EORVC, EORHI, EORLS, EORGE, EORLT, EORGT, EORLE, \
    EORS, EORSEQ, EORSNE, EORSCS, EORSHS, EORSCC, EORSLO, EORSMI, EORSPL, \
    EORSVS, EORSVC, EORSHI, EORSLS, EORSGE, EORSLT, EORSGT, EORSLE, \
    LSL, LSR, ASR, \
    CMP, CMPEQ, CMPNE, CMPCS, CMPHS, CMPCC, CMPLO, CMPMI, CMPPL, CMPVS, \
    CMPVC, CMPHI, CMPLS, CMPGE, CMPLT, CMPGT, CMPLE, \
    TEQ, TEQEQ, TEQNE, TEQCS, TEQHS, TEQCC, TEQLO, TEQMI, TEQPL, TEQVS, \
    TEQVC, TEQHI, TEQLS, TEQGE, TEQLT, TEQGT, TEQLE, \
    TST, TSTEQ, TSTNE, TSTCS, TSTHS, TSTCC, TSTLO, TSTMI, TSTPL, TSTVS, \
    TSTVC, TSTHI, TSTLS, TSTGE, TSTLT, TSTGT, TSTLE, \
    TEQ, TEQEQ, TEQNE, TEQCS, TEQHS, TEQCC, TEQLO, TEQMI, TEQPL, TEQVS, \
    TEQVC, TEQHI, TEQLS, TEQGE, TEQLT, TEQGT, TEQLE, \
    MOV, MOVEQ, MOVNE, MOVCS, MOVHS, MOVCC, MOVLO, MOVMI, MOVPL, MOVVS, \
    MOVVC, MOVHI, MOVLS, MOVGE, MOVLT, MOVGT, MOVLE, \
    MOVS, MOVSEQ, MOVSNE, MOVSCS, MOVSHS, MOVSCC, MOVSLO, MOVSMI, MOVSPL, \
    MOVSVS, MOVSVC, MOVSHI, MOVSLS, MOVSGE, MOVSLT, MOVSGT, MOVSLE, \
    LDR, LDRH, LDRSH, LDRB, LDRSB, \
    STR, STRB, STRH, \
    B, BEQ, BNE, BCS, BHS, BCC, BLO, BMI, BPL, BVS, BVC, BHI, BLS, BGE, BLT, BGT, BLE, \
    BKPT

from peachpy.arm.vfpneon import VADD, VADDL, VSUB, VSUBL, VMUL, VMULL, VMIN, VMAX, \
    VABD, VABS, VACGE, VACGT, VACLE, VACLT, \
    VAND, VBIC, VORR, VORN, VEOR, \
    VPADD, VPMIN, VPMAX, VQADD, VQSUB, VHADD, VHSUB, VRHADD, \
    VRECPS, VRSQRTS, \
    VTST, VNMUL, VDIV, VSQRT, VNEG, \
    VMLA, VMLS, VNMLA, VNMLS, VFMA, VFMS, VFNMA, VFNMS, \
    VLDR, VSTR, VLDM, VLDMIA, VLDMDB, VSTM, VSTMIA, VSTMDB, VLD1, VST1, VMOV

__m64 = peachpy.Type("__m64", size=8, is_vector=True, header="mmintrin.h")
