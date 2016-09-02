from taipan.simulate.simulate import test_redshift_success
import logging
import numpy as np

if __name__ == '__main__':
    # Generate test array
    testarr = np.zeros(30, dtype=[('target_id', 'int'),
                                  ('is_vpec_target', np.dtype(bool)),
                                  ('is_H0_target', np.dtype(bool)),
                                  ('is_lowz_target', np.dtype(bool))])
    for i in range(len(testarr)):
        testarr[i]['target_id'] = i
    visits = np.ones((30,), dtype=int)

    # Construct single-type targets
    # Recall the ordering is vpec, H0, lowz
    testarr[1]['is_H0_target'] = True
    testarr[2]['is_lowz_target'] = True
    testarr[3:6]['is_vpec_target'] = True
    for i in range(3,6):
        visits[i] = i - 3 + 1

    # Construct two-type targets
    testarr[6]['is_H0_target'] = True
    testarr[6]['is_lowz_target'] = True
    testarr[7:10]['is_H0_target'] = True
    testarr[7:10]['is_vpec_target'] = True
    for i in range(7,10):
        visits[i] = i - 7 + 1
    testarr[10:13]['is_lowz_target'] = True
    testarr[10:13]['is_vpec_target'] = True
    for i in range(10,13):
        visits[i] = i - 10 + 1

    # Construct all-type target
    testarr[13:16]['is_H0_target'] = True
    testarr[13:16]['is_vpec_target'] = True
    testarr[13:16]['is_lowz_target'] = True
    for i in range(13,16):
        visits[i] = i - 13 + 1

    # Trim the test arrays to what was used
    testarr = testarr[:16]
    visits = visits[:16]
    # print testarr
    # print visits

    # Run test_redshift_success across the system
    result = test_redshift_success(testarr, visits)
    # print result

    # Pretty-print results
    print 'No-type target (100%%):        %r' % result[0]
    print 'H0 only (100%%):               %r' % result[1]
    print 'lowz only (80%%):              %r' % result[2]
    print 'vpec only, 1 pass (30%%):      %r' % result[3]
    print 'vpec only, 2 pass (70%%):      %r' % result[4]
    print 'vpec only, 3 pass (100%%):     %r' % result[5]
    print 'H0 and lowz (80%%):            %r' % result[6]
    print 'H0 and vpec, 1 pass (30%%):    %r' % result[7]
    print 'H0 and vpec, 2 pass (70%%):    %r' % result[8]
    print 'H0 and vpec, 3 pass (100%%):   %r' % result[9]
    print 'lowz and vpec, 1 pass (30%%):  %r' % result[10]
    print 'lowz and vpec, 2 pass (70%%):  %r' % result[11]
    print 'lowz and vpec, 3 pass (100%%): %r' % result[12]
    print 'All types, 1 pass (30%%):      %r' % result[13]
    print 'All types, 1 pass (70%%):      %r' % result[14]
    print 'All types, 1 pass (100%%):     %r' % result[15]